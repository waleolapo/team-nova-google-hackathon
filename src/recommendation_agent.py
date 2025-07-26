from src.executor import Executor

class RecommendationAgent:
    def __init__(self):
        self.executor = Executor()

    def run(self, context):
        prompt = (
            "Based on the following weather, soil, and market data, provide comprehensive recommendations for suitable crops for this region. "
            "First, list the recommended crops clearly as a bulleted list. "
            "Then, for each crop, elaborate on why it is suitable, considering the provided data. "
            "Finally, include a section for 'Crucial Next Steps' or 'Missing Information' if applicable. "
            "If specific data is unavailable, provide general but plausible crop recommendations with explanations. "
            "Weather: {weather}\n" 
            "Soil: {soil}\n" 
            "Market: {market}"
        )
        task = {
            "type": "llm_call",
            "prompt": prompt
        }
        print(f"[RecommendationAgent] Prompting Gemini with: {prompt.format(**context)}")
        recommendations = self.executor.execute_task(task, context)
        print(f"[RecommendationAgent] Raw Gemini Response: {recommendations}")
        return {"recommendations": recommendations}
