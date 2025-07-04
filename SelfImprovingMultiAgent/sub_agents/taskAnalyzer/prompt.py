"""Analyze a given task and determine approach"""

TASK_ANALYSIS_PROMPT = """

Your job is to analyze the following task and provide a structured, detailed assessment to help guide its execution.

# Your task

Carefully read the provided task description. Your analysis should include the following:

1. **Task Complexity (1-10):**
   - Rate the overall complexity of the task on a scale from 1 (very simple) to 10 (extremely complex).
   - Briefly justify your rating.

2. **Required Skills:**
   - List the key skills, knowledge areas, or technologies necessary to complete the task successfully.

3. **Potential Challenges:**
   - Identify possible obstacles, risks, or difficulties that may arise during the execution of the task.

4. **Recommended Approach:**
   - Suggest a step-by-step or high-level strategy for tackling the task, including any best practices or methodologies that should be considered.

5. **Success Criteria:**
   - Define clear, measurable criteria or deliverables that indicate the task has been completed successfully.

# Output format

Respond in the following JSON format:

{
  "complexity": <integer 1-10>,
  "complexity_justification": "<short explanation>",
  "skills": ["<skill1>", "<skill2>", ...],
  "challenges": ["<challenge1>", "<challenge2>", ...],
  "approach": "<recommended approach>",
  "success_criteria": ["<criterion1>", "<criterion2>", ...]
}

# Task to analyze


"""
