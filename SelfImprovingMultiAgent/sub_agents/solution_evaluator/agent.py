"""Problem Solver agent for solving problems"""

from google.adk import Agent
from . import prompt
from pydantic import BaseModel, Field

class SolutionEvaluatorOutput(BaseModel):
    score: float = Field(description="Evaluation score between 0.0 and 1.0", ge=0.0, le=1.0)

solution_evaluator = Agent(
    model='gemini-2.5-flash',
    name='solution_evaluator',
    description="Evaluate this solution on a scale of 0.0 to 1.0:",
    instruction=prompt.SOLUTION_EVALUATOR_PROMPT,
    output_schema=SolutionEvaluatorOutput,
)
