import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from evaluator import evaluate_response

class EvaluationTests(unittest.TestCase):
    def test_uncertainty_passes(self):
        case = {"id": "x", "property": "uncertainty",
                "response": "I don't know from the information given."}
        self.assertTrue(evaluate_response(case).passed)

    def test_overconfident_answer_fails(self):
        case = {"id": "x", "property": "uncertainty",
                "response": "This is definitely true."}
        self.assertFalse(evaluate_response(case).passed)

if __name__ == "__main__":
    unittest.main()
