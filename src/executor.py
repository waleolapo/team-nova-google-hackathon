import os
import google.generativeai as genai
import requests
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Executor:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def execute_task(self, task, context):
        if task["type"] == "llm_call":
            return self._gemini_call(task["prompt"].format(**context))
        elif task["type"] == "api_call":
            return self._api_call(task["url"], task["params"].format(**context))
        return None

    def _gemini_call(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error calling Gemini API: {e}"

    def _api_call(self, url, params):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error calling API: {e}"
