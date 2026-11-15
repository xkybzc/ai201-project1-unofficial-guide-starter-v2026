#!/usr/bin/env python3
"""
The Unofficial Guide — the same pipeline, over HTTP.

    python serve.py                          run it locally on port 5000
    gunicorn serve:app                       run it the way a host runs it

Nothing new happens in this file. It is a wrapper: a request comes in, it
hands the question to `app.py::ask_pipeline` — the exact function the command
line uses — and hands the answer back as JSON. Retrieval, the relevance gate
and the grounded prompt all still live where they lived. If you change how
your system answers, you change it in those files and this one follows.

Two routes:

    POST /ask       {"question": "..."} in, the answer and its sources out
    GET  /health    is the service up, and is there an index to search

Why this exists: `app.py` runs once and exits, which is fine on your laptop
and impossible to deploy. A hosted service has to stay up and wait for
requests. This is the smallest thing that does that.

Capstone (unit 9, shape A): every request to /ask now leaves one record in
`logs/runs.jsonl`. Answered, refused and crashed runs are logged by
`app.py::ask_pipeline`; requests rejected here for bad input never reach the
pipeline, so this file logs those itself. See `runlog.py` for the fields.
"""

import os

from flask import Flask, jsonify, request

import config

app = Flask(__name__)


@app.get("/health")
def health():
    """Is the service up, and is there an index to search?

    Two different questions, and the second one is the one that bites. A
    freshly deployed service answers this route happily while every /ask
    returns "no index" — hosts give you no disk that survives a restart, so
    the index has to be built as part of getting the service up. Checking
    here means you find that out in one request instead of five.
    """
    from store import index_exists

    ready = index_exists(config.CORPUS)
    return jsonify(
        {
            "status": "ok",
            "corpus": config.CORPUS,
            "index_ready": ready,
            "detail": (
                "ready"
                if ready
                else "no index for this corpus — run `python app.py index`"
            ),
        }
    )


@app.post("/ask")
def ask():
    """One question in, one grounded answer out.

    A refused question is a 200, not an error. The gate refusing is your
    system working — it is an answer, and the JSON says so with
    `"refused": true` so whatever calls this can tell the two apart.
    """
    import time

    import run_log
    from app import ask_pipeline

    started = time.perf_counter()
    payload = request.get_json(silent=True) or {}
    raw = payload.get("question") if isinstance(payload, dict) else None
    question = raw.strip() if isinstance(raw, str) else ""

    if not question:
        message = (
            "Send JSON with a question in it, like "
            '{"question": "is the housing lottery random?"}'
        )
        row = run_log.write(
            {
                "ts": run_log.now_iso(),
                "run_id": run_log.new_run_id(),
                "entrypoint": "http",
                "status": "rejected",
                # What actually arrived, so a bad client can be diagnosed later.
                "question": repr(raw) if raw is not None else request.get_data(as_text=True)[:200],
                "answer": None,
                "duration_ms": round((time.perf_counter() - started) * 1000, 1),
                "retrieve_ms": None,
                "generate_ms": 0.0,
                "model_calls": 0,
                "cache_hit": False,
                "prompt_tokens": 0,
                "output_tokens": 0,
                "error": "rejected input: no question",
                "http_status": 400,
            }
        )
        return jsonify({"error": message, "run_id": row["run_id"]}), 400

    try:
        outcome = ask_pipeline(question, corpus=config.CORPUS, entrypoint="http")
    except Exception as exc:  # noqa: BLE001 — a reader gets this, not a traceback
        # ask_pipeline has already written the error record before re-raising.
        return (
            jsonify(
                {
                    "error": f"{type(exc).__name__}: {exc}",
                    "run_id": getattr(exc, "run_id", None),
                }
            ),
            500,
        )

    return jsonify(
        {
            "question": question,
            "answer": outcome["answer"],
            "refused": outcome["refused"],
            "sources": outcome["sources"],
            "best_distance": round(outcome["best_distance"], 4),
            "threshold": outcome["threshold"],
            "corpus": config.CORPUS,
            "run_id": outcome["run_id"],
            "duration_ms": outcome["duration_ms"],
        }
    )


def main():
    # Hosts tell you which port to listen on through PORT, and they expect you
    # on 0.0.0.0. Binding 127.0.0.1 instead works perfectly on your laptop and
    # then answers nothing at all once deployed, because the host's router
    # can't reach a socket that only accepts connections from inside the
    # container. It is the single most common way a first deploy "succeeds"
    # and is unreachable.
    port = int(os.getenv("PORT", "5000"))

    # Debug mode reloads on save, which is handy, and prints a console that
    # runs arbitrary code, which is not something to leave switched on where
    # strangers can reach it. Off unless you ask for it.
    debug = os.getenv("AI201_DEBUG", "0") == "1"

    # Capstone: on a clean checkout there is no index (chroma_db/ is
    # gitignored), so build one before serving. This is what makes
    # `python serve.py` the single start command in RUNNING.md.
    from store import index_exists

    if not index_exists(config.CORPUS):
        import time

        from chunker import split_documents
        from ingest import load_documents
        from store import build_index

        print(f"No index for '{config.CORPUS}' yet — building it (first run "
              f"also downloads the ~80 MB embedding model)...")
        t0 = time.perf_counter()
        count = build_index(split_documents(load_documents(config.CORPUS)),
                            corpus=config.CORPUS)
        print(f"Indexed {count} chunks in {time.perf_counter() - t0:.1f}s\n")

    print(f"Serving The Unofficial Guide on http://localhost:{port}")
    print(f"Corpus: {config.CORPUS}    (Ctrl-C to stop)\n")
    print("Try it from another terminal:\n")
    print(f"  curl http://localhost:{port}/health")
    print(
        f"  curl -X POST http://localhost:{port}/ask \\\n"
        f"    -H 'Content-Type: application/json' \\\n"
        f"    -d '{{\"question\": \"is the housing lottery random?\"}}'\n"
    )

    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    main()