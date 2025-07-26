from src.executor import Executor

class TranslationAgent:
    def __init__(self):
        self.executor = Executor()

    def run(self, context):
        language = context.get("language", "English") # Default to English
        
        # Ensure 'recommendations' is in context, even if empty
        if "recommendations" not in context:
            context["recommendations"] = ""

        prompt = (
            "Translate the following recommendations to {language}. "
            "Recommendations: {recommendations}"
        )
        task = {
            "type": "llm_call",
            "prompt": prompt
        }
        translated_text = self.executor.execute_task(task, context)
        return {"translated_response": translated_text}
