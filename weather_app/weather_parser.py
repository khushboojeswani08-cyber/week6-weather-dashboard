
from datetime import datetime


class WeatherParser:

    @staticmethod
    def parse_current_weather(data):
        if not data:
            return None

        try:
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
                "wind_speed": data["wind"]["speed"],
                "icon": data["weather"][0]["icon"]
            }
        except (KeyError, IndexError, TypeError):
            return None

    @staticmethod
    def parse_forecast(data):
        if not data or "list" not in data:
            return []

        forecast = []

        try:
            for item in data["list"]:
                timestamp = item["dt"]
                date = datetime.fromtimestamp(timestamp)

                if date.hour == 12:
                    forecast.append({
                        "date": date.strftime("%d %b"),
                        "temperature": item["main"]["temp"],
                        "description": item["weather"][0]["description"].title(),
                        "humidity": item["main"]["humidity"],
                        "wind_speed": item["wind"]["speed"],
                        "icon": item["weather"][0]["icon"]
                    })

            return forecast[:5]

        except (KeyError, IndexError, TypeError, ValueError):
            return []
          
