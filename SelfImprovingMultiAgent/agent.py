from google.adk.agents import LlmAgent
from google.adk.agents import SequentialAgent

from .sub_agents.taskAnalyzer import task_analyzer

self_improving_agent = SequentialAgent(
    name="self_improving_agent",
    description="An agent that solves problems and improves itself over time.",
    sub_agents=[task_analyzer],
)

root_agent = self_improving_agent