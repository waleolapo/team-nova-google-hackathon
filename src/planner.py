import json
import re
from src.executor import Executor

class Planner:
    def __init__(self):
        self.executor = Executor()

    def plan(self, query, agents):
        example_plan_dict = {"agent": "Data Agent", "task": "Get weather data"}
        example_plan_str = json.dumps([example_plan_dict]).replace('{', '{{').replace('}', '}}')

        prompt = (
            f'Based on the query "{query}", create a plan of tasks to be executed by the following agents: {list(agents.keys())}. '
            f'The plan should be a list of dictionaries, where each dictionary has "agent" and "task" keys. '
            f'For example: {example_plan_str}'
        )
        task = {
            "type": "llm_call",
            "prompt": prompt
        }
        plan_raw_response = self.executor.execute_task(task, {})
        
        try:
            # Attempt to find a JSON array in the response
            match = re.search(r'\[.*\]', plan_raw_response, re.DOTALL)
            if match:
                plan_str = match.group(0)
                plan = json.loads(plan_str)
                return plan
            else:
                raise ValueError("No JSON array found in LLM response")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error parsing LLM response: {e}. Raw response: {plan_raw_response}")
            # Fallback to a default plan if the LLM fails to generate a valid one or if parsing fails
            return [
                {"agent": "Data Agent", "task": "Get weather data"},
                {"agent": "Recommendation Agent", "task": "Get crop recommendations"},
                {"agent": "Translation Agent", "task": "Translate response"}
            ]