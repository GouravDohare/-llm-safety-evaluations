import json
import sys
from evaluator import evaluate

if len(sys.argv) != 2:
    raise SystemExit("Usage: python src/run_eval.py examples/sample_outputs.json")

with open(sys.argv[1], encoding="utf-8") as f:
    cases = json.load(f)

results, rate = evaluate(cases)

for r in results:
    print(f"{r.case_id}: {'PASS' if r.passed else 'FAIL'} — {r.reason}")

print(f"\nPass rate: {rate:.1%}")
