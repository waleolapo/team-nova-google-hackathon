# Architecture

The FarmWise AI system is built on a multi-agent architecture, where each agent has a specific role and responsibility.

```
+-----------------+      +--------------------+      +----------------------+
|  Interface Agent  |----->|  Coordinator Agent   |----->|      Data Agent      |
+-----------------+      +--------------------+      +----------------------+
                           |                     |      +----------------------+
                           |                     +----->|  Recommendation Agent  |
                           |                           +----------------------+
                           |                     +----->|   Translation Agent    |
                           +---------------------+      +----------------------+
```

-   **Interface Agent:** Parses user queries and extracts key information (location, language).
-   **Coordinator Agent:** Orchestrates the workflow between all other agents.
-   **Data Agent:** Fetches real-time data from external APIs (e.g., OpenWeatherMap) and provides mock soil/market data. Designed to be adaptable to various locations.
-   **Recommendation Agent:** Generates farming advice based on provided data.
-   **Translation Agent:** Translates the advice into the user's language (defaults to English).

## Core Modules

-   **planner.py:** Implements the ReAct pattern to plan tasks using Gemini.
-   **executor.py:** Manages API calls (Gemini, OpenWeatherMap) and handles errors.
-   **memory.py:** Stores user context and logs in JSON files.