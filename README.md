
# Weather Dashboard Application

## Project Description
A Python application that fetches current weather information and a 5-day forecast using the OpenWeatherMap API.

## Features
- Current weather for any city
- Temperature and feels-like temperature
- Humidity and wind speed
- Weather conditions
- 5-day weather forecast
- API error handling
- Caching to reduce repeated requests

## Technologies Used
- Python
- Requests
- Python-dotenv
- OpenWeatherMap API

## Project Structure
- weather_app/
  - __init__.py
  - config.py
  - weather_api.py
  - weather_parser.py
  - weather_display.py
- main.py
- requirements.txt
- .env.example
- README.md

## Setup Instructions
1. Install Python 3.
2. Install dependencies using:
   pip install -r requirements.txt
3. Create a .env file in the project root.
4. Add your API key:
   OPENWEATHER_API_KEY=your_api_key_here
5. Run the application:
   python main.py

## API Setup
Get an API key from https://openweathermap.org/api

Never upload your real API key to GitHub.

## Author
Khushboo Jeswani

