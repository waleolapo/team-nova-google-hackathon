import os
from src.executor import Executor

class DataAgent:
    def __init__(self):
        self.executor = Executor()

    def run(self, context):
        location = context.get("location", "Lagos")
        task = {
            "type": "api_call",
            "url": "http://api.openweathermap.org/data/2.5/weather",
            "params": f"q={location}&appid={os.getenv('OPENWEATHER_API_KEY')}"
        }
        weather_data = self.executor.execute_task(task, context)

        # Mock soil and market data for Lagos
        soil_data = {"type": "sandy loam", "ph": 6.5, "organic_matter": "2.5%"}
        market_data = {"yam": "$2/kg", "cassava": "$1.5/kg", "maize": "$1/kg"}

        return {"weather": weather_data, "soil": soil_data, "market": market_data}
