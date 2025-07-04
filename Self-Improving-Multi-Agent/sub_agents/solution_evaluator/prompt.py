"""Evaluate this solution on a scale of 0.0 to 1.0:"""

SOLUTION_EVALUATOR_PROMPT = """
Evaluate this solution on a scale of 0.0 to 1.0:
{solution}
Rate based on:
1. Completeness (addresses all aspects)
2. Correctness (logically sound)
3. Clarity (well explained)
4. Practicality (implementable)
5. Innovation (creative approach)

Respond with just a decimal number between 0.0 and 1.0.
"""

