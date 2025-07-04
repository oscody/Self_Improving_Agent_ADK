"""Critic agent for identifying and verifying statements using search tools."""

from pydantic import BaseModel, Field
from google.adk import Agent
from . import prompt


class TaskAnalysisOutput(BaseModel):
    complexity: int = Field(description="Task complexity score from 1-10", ge=1, le=10)
    skills: list[str] = Field(description="List of required skills for the task")
    challenges: list[str] = Field(description="List of potential challenges")
    approach: str = Field(description="Recommended approach for the task")
    success_criteria: list[str] = Field(description="List of success criteria")


task_analyzer = Agent(
    model='gemini-2.5-flash',
    name='task_analyzer',
    description="Analyze a given task and determine approach",
    instruction=prompt.TASK_ANALYSIS_PROMPT,
    output_schema=TaskAnalysisOutput,
)
