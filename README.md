# LLM Safety Evaluations

A small, reproducible evaluation harness for testing predefined behavioural properties of language-model outputs.

## Goal

Instead of asking whether a model is simply "safe", this project treats safety as a set of explicit, testable properties. The initial evaluator checks supplied model responses against simple criteria and reports pass rates.

## Design

1. Store prompts and model responses as data.
2. Apply deterministic evaluators.
3. Report each case and aggregate pass rate.
4. Keep failure cases visible rather than hiding them in a single score.

The initial checks are intentionally simple. They are a framework for developing stronger evaluations, not evidence that a model is safe.

## Run

```bash
python src/run_eval.py examples/sample_outputs.json
python -m unittest discover -s tests -v
```

## Important limitation

Keyword and rule-based evaluation can produce false positives and false negatives. A serious evaluation should use carefully specified rubrics, adversarial test generation, multiple evaluators where appropriate, and human review of important failures.
