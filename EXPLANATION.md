# Explanation

## ReAct Pattern

The Coordinator Agent uses the ReAct (Reasoning + Acting) pattern to break down complex queries into a series of tasks. This allows the system to handle a wide range of user inputs in a structured and efficient manner. The Planner now leverages the Gemini API for more intelligent task prioritization.

## Memory

The system uses a JSON-based memory (`data/memory.json`) to store user context (e.g., location, language) and `data/logs.json` for interaction logs. This allows the system to maintain a history of user interactions and provide more personalized recommendations over time.

## Gemini and OpenWeatherMap Integration

-   **Gemini 2.5 Flash:** Used for query parsing, intelligent task planning, recommendation generation, and translations.
-   **OpenWeatherMap API:** Provides real-time weather data for specified locations. Mock soil and market data are also integrated, and would need to be replaced with real-time, location-specific data sources for a production environment.

## Global Applicability

FarmWise AI is designed to be globally applicable. While Lagos, Nigeria, is used as a prominent example in the documentation and sample workflows, the system can process queries for various locations and languages. The `Interface Agent` extracts location and language from the user's query, and the `Translation Agent` defaults to English if no specific language is requested.

## Limitations

-   The system's effectiveness is dependent on the availability and accuracy of external APIs.
-   Soil and market data are currently mocked and would need to be replaced with real-time, location-specific data sources for a production environment.

## Sample Query Flow (using Lagos as an example)

1.  **User:** "What crops for my farm in Lagos?"
2.  **Interface Agent:** Parses query with Gemini, extracts "Lagos" as location and defaults to "English" as language.
3.  **Coordinator Agent:** Plans tasks (fetch weather, recommend crops, translate) using Gemini-powered planner.
4.  **Data Agent:** Fetches Lagos weather via OpenWeatherMap and provides mock soil/market data.
5.  **Recommendation Agent:** Suggests crops (e.g., yam, cassava) using Gemini, considering weather, soil, and market data.
6.  **Translation Agent:** Translates the advice to English (or the user's specified language) using Gemini.
7.  **Flask:** Displays the recommendations to the user.