from src.planner import Planner
from src.interface_agent import InterfaceAgent
from src.data_agent import DataAgent
from src.recommendation_agent import RecommendationAgent
from src.translation_agent import TranslationAgent
from src.memory import Memory
import json
import re

class CoordinatorAgent:
    def __init__(self):
        self.planner = Planner()
        self.memory = Memory()
        self.agents = {
            "Interface Agent": InterfaceAgent(),
            "Data Agent": DataAgent(),
            "Recommendation Agent": RecommendationAgent(),
            "Translation Agent": TranslationAgent(),
        }

    def run(self, query):
        # For demonstration, using a fixed user_id. In a real app, this would be dynamic.
        user_id = "test_user"
        context = self.memory.get_user_context(user_id)
        context["query"] = query

        # Parse query to get location and language
        interface_agent = self.agents["Interface Agent"]
        parsed_query_result = interface_agent.run(context)
        
        parsed_query = {}
        try:
            if isinstance(parsed_query_result, dict) and 'parsed_query' in parsed_query_result:
                # Remove markdown code block fences if present
                json_string = re.sub(r'```json\n|```', '', parsed_query_result['parsed_query']).strip()
                parsed_query = json.loads(json_string)
            context.update(parsed_query)
        except (json.JSONDecodeError, KeyError, Exception) as e:
            print(f"Error parsing Interface Agent response: {e}. Raw response: {parsed_query_result}")
            # fallback to default values
            context["location"] = None # No default location
            context["language"] = "English" # Default to English

        plan = self.planner.plan(query, self.agents)

        for step in plan:
            agent = self.agents[step["agent"]]
            result = agent.run(context)
            context.update(result)

            # Special handling for Recommendation Agent output before passing to Translation Agent
            if step["agent"] == "Recommendation Agent" and "recommendations" in context:
                full_recommendation_text = context["recommendations"]
                # Extract bulleted list of recommendations
                match = re.search(r'^\*\s.*(?:\n\*\s.*)*', full_recommendation_text, re.MULTILINE)
                if match:
                    concise_recommendations = match.group(0)
                    context["recommendations"] = concise_recommendations # Overwrite for translation
                else:
                    # If no bulleted list found, use the full text but log a warning
                    print("Warning: No bulleted list found in Recommendation Agent output. Translating full text.")

        return context.get("translated_response", context.get("recommendations", "No recommendations found."))