from google.adk.agents import LlmAgent
from google.adk.agents import SequentialAgent

from .sub_agents.task_analyzer import task_analyzer
from .sub_agents.problem_solver import problem_solver
from .sub_agents.solution_evaluator import solution_evaluator

self_improving_agent = SequentialAgent(
    name="self_improving_agent",
    description="The primary research assistant that solves problems and improves itself over time.",
    sub_agents=[task_analyzer, problem_solver, solution_evaluator],
)



root_agent = LlmAgent(
    name="assistant",
    model="gemini-2.0-flash",    
    description="The primary assistant",
    instruction=f"""
    ""Greet the user and ask them what they would like to do today.""",
    sub_agents=[self_improving_agent],
)

