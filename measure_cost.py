#!/usr/bin/env python3
"""
Measure what one run costs — capstone (unit 9), shape A.

    python measure_cost.py                  10 runs, caching off
    python measure_cost.py --runs 20
    python measure_cost.py --price-in 0.10 --price-out 0.40
                                            also convert tokens to dollars

It cycles through your QUESTIONS in questions.py, sends each one through
`app.py::ask_pipeline` — the same function `serve.py` calls — with the cache
off, and then reads the records those runs wrote to `logs/runs.jsonl`.

Every number it reports comes off those records, which means it comes off the
responses: token counts are what the service said it used, and durations are
wall-clock time on this machine. Refused runs make no model call and cost 0
tokens; they are counted separately so they don't drag the average down
without you noticing.

It writes a short report to results/cost_<timestamp>.md. Commit it.
"""

import argparse
import datetime as dt
import sys

import config
import questions as qs


def mean(values):
    values = [v for v in values if isinstance(v, (int, float))]
    return sum(values) / len(values) if values else 0.0


def main():
    parser = argparse.ArgumentParser(description="Measure the cost of one run.")
    parser.add_argument("--runs", type=int, default=10)
    parser.add_argument("--price-in", type=float, default=None,
                        help="USD per 1M input tokens (optional)")
    parser.add_argument("--price-out", type=float, default=None,
                        help="USD per 1M output tokens (optional)")
    args = parser.parse_args()

    import runlog
    from app import ask_pipeline

    items = qs.answered()
    if not items:
        sys.exit("questions.py has no questions in it.")

    run_ids = []
    for i in range(args.runs):
        question = items[i % len(items)]["question"]
        try:
            outcome = ask_pipeline(question, entrypoint="cost", cache=False)
            run_ids.append(outcome["run_id"])
            print(f"  run {i + 1:>2}: {outcome['duration_ms']:>8.1f} ms  "
                  f"{'refused' if outcome['refused'] else 'answered'}  {question}")
        except Exception as exc:  # noqa: BLE001 — still logged; keep measuring
            run_ids.append(getattr(exc, "run_id", None))
            print(f"  run {i + 1:>2}: ERROR {type(exc).__name__}: {exc}")

    wanted = {r for r in run_ids if r}
    rows = [r for r in runlog.read() if r.get("run_id") in wanted]
    answered = [r for r in rows if r.get("status") == "ok"]
    refused = [r for r in rows if r.get("status") == "refused"]
    errors = [r for r in rows if r.get("status") == "error"]
    cached = [r for r in answered if r.get("cache_hit")]

    p_in = mean([r.get("prompt_tokens") for r in answered])
    p_out = mean([r.get("output_tokens") for r in answered])
    dur = mean([r.get("duration_ms") for r in answered])
    ret = mean([r.get("retrieve_ms") for r in answered])
    gen = mean([r.get("generate_ms") for r in answered])

    lines = [
        "# Cost of one run",
        "",
        f"- Produced by: `measure_cost.py::main`, reading `logs/runs.jsonl`",
        f"- When: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"- Model: `{config.MODEL}` · corpus `{config.CORPUS}` · top-k {config.TOP_K}",
        f"- Runs: {len(rows)} logged ({len(answered)} answered, {len(refused)} refused, "
        f"{len(errors)} errors), caching off ({len(cached)} cache hits)",
        f"- Run ids: {', '.join(r for r in run_ids if r)}",
        "",
        "Averages over the answered runs:",
        "",
        "| Measure | Mean per run |",
        "|---|---|",
        f"| Input tokens | {p_in:.1f} |",
        f"| Output tokens | {p_out:.1f} |",
        f"| Total tokens | {p_in + p_out:.1f} |",
        f"| Total duration | {dur:.1f} ms |",
        f"| Retrieval (embed + search) | {ret:.1f} ms |",
        f"| Generation (model call) | {gen:.1f} ms |",
    ]

    if args.price_in is not None and args.price_out is not None:
        dollars = p_in / 1e6 * args.price_in + p_out / 1e6 * args.price_out
        lines += [
            "",
            f"At ${args.price_in}/1M input and ${args.price_out}/1M output tokens "
            f"(prices entered by hand, not measured):",
            f"{p_in:.1f} × {args.price_in}/1e6 + {p_out:.1f} × {args.price_out}/1e6 "
            f"= **${dollars:.6f} per answered run**",
        ]

    lines += ["", "Raw records:", "", "```"]
    lines += [__import__("json").dumps(r, ensure_ascii=False) for r in rows]
    lines += ["```", ""]

    config.RESULTS_DIR.mkdir(exist_ok=True)
    path = config.RESULTS_DIR / f"cost_{dt.datetime.now().strftime('%Y-%m-%d_%H%M')}.md"
    path.write_text("\n".join(lines), encoding="utf-8")

    print()
    print("\n".join(lines[5:lines.index("Raw records:")]).rstrip())
    shown = path.relative_to(config.ROOT) if path.is_relative_to(config.ROOT) else path
    print(f"\nWrote {shown} — commit it.")


if __name__ == "__main__":
    main()