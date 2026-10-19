
import requests
import time

from .config import API_KEY, BASE_URL, DEFAULT_UNITS, CACHE_DURATION


class WeatherAPI:
    def __init__(self):
        self.cache = {}

    def make_request(self, endpoint, params):
        if not API_KEY:
            print("Error: API key is missing.")
            return None

        params["appid"] = API_KEY
        params["units"] = DEFAULT_UNITS

        try:
            response = requests.get(
                f"{BASE_URL}/{endpoint}",
                params=params,
                timeout=10
            )

            if response.status_code == 200:
                return response.json()

            elif response.status_code == 401:
                print("Error: Invalid API key.")
            elif response.status_code == 404:
                print("Error: City not found.")
            elif response.status_code == 429:
                print("Error: API rate limit exceeded.")
            else:
                print(f"Error: HTTP {response.status_code}")

        except requests.exceptions.Timeout:
            print("Error: Request timed out.")
        except requests.exceptions.ConnectionError:
            print("Error: Check your internet connection.")
        except requests.exceptions.RequestException as error:
            print(f"Request error: {error}")

        return None

    def get_current_weather(self, city):
        cache_key = f"current_{city.lower()}"
        now = time.time()

        if cache_key in self.cache:
            data, saved_time = self.cache[cache_key]
            if now - saved_time < CACHE_DURATION:
                return data

        data = self.make_request(
            "weather",
            {"q": city}
        )

        if data:
            self.cache[cache_key] = (data, now)

        return data

    def get_forecast(self, city):
        cache_key = f"forecast_{city.lower()}"
        now = time.time()

        if cache_key in self.cache:
            data, saved_time = self.cache[cache_key]
            if now - saved_time < CACHE_DURATION:
                return data

        data = self.make_request(
            "forecast",
            {"q": city}
        )

        if data:
            self.cache[cache_key] = (data, now)

        return data
      
