from src.executor import Executor

class InterfaceAgent:
    def __init__(self):
        self.executor = Executor()

    def run(self, context):
        query = context.get("query")
        prompt = (
            f'Extract the location and language from the following query: "{query}". '
            f'Return the answer as a JSON object with "location" and "language" keys. Default language to English if not specified.'
        )
        task = {
            "type": "llm_call",
            "prompt": prompt
        }
        parsed_query = self.executor.execute_task(task, context)
        return {"parsed_query": parsed_query}
