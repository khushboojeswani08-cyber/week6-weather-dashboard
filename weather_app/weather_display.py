
class WeatherDisplay:

    @staticmethod
    def show_current_weather(weather):
        if not weather:
            print("Weather data is not available.")
            return

        print("\n" + "=" * 35)
        print("       CURRENT WEATHER")
        print("=" * 35)
        print(f"City: {weather['city']}, {weather['country']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Feels like: {weather['feels_like']} °C")
        print(f"Condition: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind speed: {weather['wind_speed']} m/s")
        print("=" * 35)

    @staticmethod
    def show_forecast(forecast):
        if not forecast:
            print("Forecast data is not available.")
            return

        print("\n" + "=" * 45)
        print("          5-DAY WEATHER FORECAST")
        print("=" * 45)

        for day in forecast:
            print(f"\nDate: {day['date']}")
            print(f"Temperature: {day['temperature']} °C")
            print(f"Condition: {day['description']}")
            print(f"Humidity: {day['humidity']}%")
            print(f"Wind speed: {day['wind_speed']} m/s")

        print("\n" + "=" * 45)
      
