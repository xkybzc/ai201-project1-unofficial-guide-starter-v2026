"""

Every question that goes through the system leaves exactly one line in
`logs/runs.jsonl`: one JSON object per line, with named fields. That includes
runs that were refused by the gate, runs that crashed, and requests that were
rejected before they reached the pipeline. A failure that only shows up as an
absence is one you'll never find.

Fields on every record:

    ts              when the run started, ISO 8601, UTC
    run_id          short random id, so one run can be found again
    entrypoint      "cli", "http", or "cost" — what started the run
    status          "ok", "refused", "rejected" (bad input), or "error"
    question        what came in
    answer          what went out (the refusal text when refused)
    duration_ms     total wall-clock time for the run
    retrieve_ms     embedding the question + searching the index
    generate_ms     the model call (0 when refused — no call is made)
    best_distance   the gate's input; lower is closer
    threshold       the gate's cutoff for this run
    sources         files retrieved
    model_calls     calls this run made to the model service (0 or 1, more on retry)
    cache_hit       true if the answer came from the local cache (cost 0 tokens)
    prompt_tokens   tokens in, as reported by the service for this run
    output_tokens   tokens out, as reported by the service for this run
    error           "ExceptionType: message" when status is "error", else null
    http_status     set for entrypoint "http"

Read it back with:

    python runlog.py tail            last 10 records, one per line
    python runlog.py tail -n 20
    python runlog.py summary         counts by status, mean durations and tokens
"""

import argparse
import datetime as dt
import json
import os
import threading
import uuid
from pathlib import Path

import config

LOG_DIR = Path(os.getenv("AI201_LOG_DIR", str(config.ROOT / "logs")))
LOG_FILE = LOG_DIR / "runs.jsonl"

# Field order is fixed so pasted entries are easy to read side by side.
FIELDS = [
    "ts", "run_id", "entrypoint", "status", "question", "answer",
    "duration_ms", "retrieve_ms", "generate_ms",
    "best_distance", "threshold", "sources",
    "model_calls", "cache_hit", "prompt_tokens", "output_tokens",
    "error", "http_status",
]

_lock = threading.Lock()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds")


def new_run_id() -> str:
    return uuid.uuid4().hex[:8]


def write(record: dict) -> dict:
    """Append one record. Never raises — logging must not break a run."""
    row = {field: record.get(field) for field in FIELDS}
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        line = json.dumps(row, ensure_ascii=False)
        with _lock, open(LOG_FILE, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except Exception:  # noqa: BLE001 — accounting never breaks the thing it accounts for
        pass
    return row


def read(path: Path = LOG_FILE) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # a half-written line from a killed process
    return rows


def _mean(values):
    values = [v for v in values if isinstance(v, (int, float))]
    return sum(values) / len(values) if values else None


def summarize(rows: list[dict]) -> str:
    if not rows:
        return "No runs logged yet."
    by_status: dict[str, int] = {}
    for r in rows:
        by_status[r.get("status") or "?"] = by_status.get(r.get("status") or "?", 0) + 1

    answered = [r for r in rows if r.get("status") == "ok" and not r.get("cache_hit")]
    lines = [
        f"{len(rows)} runs in {LOG_FILE.relative_to(config.ROOT) if LOG_FILE.is_relative_to(config.ROOT) else LOG_FILE}",
        "by status: " + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items())),
    ]

    def fmt(label, value, unit=""):
        return f"  {label:<28} {value:.1f}{unit}" if value is not None else f"  {label:<28} —"

    lines.append(f"answered, uncached ({len(answered)} runs):")
    lines.append(fmt("mean duration", _mean([r.get("duration_ms") for r in answered]), " ms"))
    lines.append(fmt("mean retrieve", _mean([r.get("retrieve_ms") for r in answered]), " ms"))
    lines.append(fmt("mean generate", _mean([r.get("generate_ms") for r in answered]), " ms"))
    lines.append(fmt("mean prompt tokens", _mean([r.get("prompt_tokens") for r in answered])))
    lines.append(fmt("mean output tokens", _mean([r.get("output_tokens") for r in answered])))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Read the structured run log.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_tail = sub.add_parser("tail", help="print the last N records, one JSON object per line")
    p_tail.add_argument("-n", type=int, default=10)
    p_tail.add_argument("--status", help="only records with this status, e.g. error")
    sub.add_parser("summary", help="counts and means")
    args = parser.parse_args()

    rows = read()
    if args.cmd == "tail":
        if args.status:
            rows = [r for r in rows if r.get("status") == args.status]
        for r in rows[-args.n:]:
            print(json.dumps(r, ensure_ascii=False))
        if not rows:
            print("No matching runs logged yet.")
    else:
        print(summarize(rows))


if __name__ == "__main__":
    main()