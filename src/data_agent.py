import os
from src.executor import Executor

class DataAgent:
    def __init__(self):
        self.executor = Executor()

    def run(self, context):
        location = context.get("location")
        weather_data = {}

        if location:
            task = {
                "type": "api_call",
                "url": "http://api.openweathermap.org/data/2.5/weather",
                "params": f"q={location}&appid={os.getenv('OPENWEATHER_API_KEY')}"
            }
            api_response = self.executor.execute_task(task, context)
            
            if isinstance(api_response, dict) and api_response.get("cod") == 200:
                weather_data = api_response
            else:
                print(f"[DataAgent] Error fetching weather for {location}: {api_response}")
                weather_data = {"error": f"Could not retrieve weather for {location}. {api_response}"}
        else:
            print("[DataAgent] No location provided for weather data.")
            weather_data = {"error": "No location provided."}

        print(f"[DataAgent] Weather Data: {weather_data}")

        # Mock soil and market data - these would ideally be dynamic based on location
        soil_data = {"type": "generic", "ph": "variable", "organic_matter": "variable"}
        market_data = {"crop_prices": "variable"}
        print(f"[DataAgent] Soil Data: {soil_data}")
        print(f"[DataAgent] Market Data: {market_data}")

        return {"weather": weather_data, "soil": soil_data, "market": market_data}
