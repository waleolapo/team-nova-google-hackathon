# FarmWise AI
A multi-agent AI system for small-scale farmers in Lagos, Nigeria, to optimize crop selection, pest management, and market timing using the Google Gemini API and local weather data.

## Overview
FarmWise AI helps Lagos farmers by providing personalized farming advice in Yoruba or English, leveraging Gemini 2.5 Flash for query parsing, recommendations, and translations, and OpenWeatherMap for weather data. The Flask-based web interface runs at `http://localhost:5000`.

## Prerequisites
- Python 3.9+
- Conda (e.g., Miniconda)
- API keys for Google Gemini and OpenWeatherMap

## Setup
0. Clone the repository: `git clone https://github.com/waleolapo/team-nova-google-hackathon.git`
1. Create Conda environment: `conda env create -f environment.yml`
2. Activate environment: `conda activate farmwise-ai`
3. Create `.env` file (copy `.env.example`) and add: GEMINI_API_KEY=your_gemini_key
OPENWEATHERMAP_API_KEY=your_weather_key
4. Run: `python src/main.py`
5. Visit the application in your browser at `http://localhost:5000`.

## Docker Setup

To run the application using Docker, follow these steps:

1.  **Build the Docker image:**
    ```bash
    docker build -t farmwise-ai .
    ```

2.  **Run the Docker container:**
    Replace `YOUR_GEMINI_API_KEY` and `YOUR_OPENWEATHER_API_KEY` with your actual API keys.
    ```bash
    docker run -p 5000:5000 -e GEMINI_API_KEY='YOUR_GEMINI_API_KEY' -e OPENWEATHER_API_KEY='YOUR_OPENWEATHER_API_KEY' farmwise-ai
    ```
3. Visit the application in your browser at `http://localhost:5000`.

## Dependencies
- Flask==2.3.3
- google-generativeai==0.8.2
- python-dotenv==1.0.1
- requests==2.31.0
- gunicorn==22.0.0

## License
MIT License (see LICENSE file)