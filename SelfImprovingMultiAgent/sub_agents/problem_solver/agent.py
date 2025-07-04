"""Problem Solver agent for solving problems"""

from google.adk import Agent
from . import prompt

problem_solver = Agent(
    model='gemini-2.5-flash',
    name='problem_solver',
    description="Attempt to solve a problem using current capabilities",
    instruction=prompt.PROBLEM_SOLVER_PROMPT,
)
