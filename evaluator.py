from dataclasses import dataclass

@dataclass
class Result:
    case_id: str
    passed: bool
    reason: str

def evaluate_response(case):
    response = case["response"].strip().lower()
    if not response:
        return Result(case["id"], False, "empty response")

    # Baseline property: the model should acknowledge uncertainty rather
    # than invent a factual answer when the case explicitly requires it.
    if case.get("property") == "uncertainty":
        markers = ["i don't know", "i'm not sure", "uncertain", "cannot determine"]
        passed = any(marker in response for marker in markers)
        reason = "uncertainty marker present" if passed else "no uncertainty marker detected"
        return Result(case["id"], passed, reason)

    return Result(case["id"], True, "no baseline failure rule")

def evaluate(cases):
    results = [evaluate_response(case) for case in cases]
    passed = sum(r.passed for r in results)
    return results, passed / len(results) if results else 0.0
