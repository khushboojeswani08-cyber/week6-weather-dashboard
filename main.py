
from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser
from weather_app.weather_display import WeatherDisplay


def main():
    print("=" * 35)
    print("      WEATHER DASHBOARD")
    print("=" * 35)

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a valid city name.")
        return

    api = WeatherAPI()

    print("\nFetching current weather...")
    current_data = api.get_current_weather(city)

    if current_data:
        current_weather = WeatherParser.parse_current_weather(
            current_data
        )
        WeatherDisplay.show_current_weather(current_weather)
    else:
        print("Could not fetch current weather.")
        return

    print("\nFetching 5-day forecast...")
    forecast_data = api.get_forecast(city)

    if forecast_data:
        forecast = WeatherParser.parse_forecast(forecast_data)
        WeatherDisplay.show_forecast(forecast)
    else:
        print("Could not fetch weather forecast.")


if __name__ == "__main__":
    main()
  
