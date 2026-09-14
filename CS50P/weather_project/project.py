import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def main():
    print("Simple Weather Program")
    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty.")
        return

    try:
        location = get_location(city)

        if location is None:
            print("City not found.")
            return

        weather = get_weather(location["latitude"], location["longitude"])

        print(f"\nWeather in {location['name']}, {location['country']}")
        print(f"Temperature: {weather['temperature']} C")
        print(f"Wind speed: {weather['wind_speed']} km/h")
        print(f"Condition: {describe_weather(weather['weather_code'])}")

    except (HTTPError, URLError, KeyError, ValueError):
        print("Internet or API error. Please try again.")


def get_location(city):
    """Find the latitude and longitude of a city."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parameters = {"name": city, "count": 1, "language": "en", "format": "json"}

    response = urlopen(url + "?" + urlencode(parameters), timeout=10)
    data = json.loads(response.read())

    if "results" not in data or len(data["results"]) == 0:
        return None

    result = data["results"][0]
    return {
        "name": result["name"],
        "country": result.get("country", "Unknown"),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }


def get_weather(latitude, longitude):
    """Get the current weather for a latitude and longitude."""
    url = "https://api.open-meteo.com/v1/forecast"
    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,wind_speed_10m",
    }

    response = urlopen(url + "?" + urlencode(parameters), timeout=10)
    current = json.loads(response.read())["current"]

    return {
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"],
    }


def describe_weather(code):
    """Change a weather code into simple text."""
    if code == 0:
        return "Clear sky"
    elif code in [1, 2, 3]:
        return "Cloudy"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55, 56, 57]:
        return "Drizzle"
    elif code in [61, 63, 65, 66, 67, 80, 81, 82]:
        return "Rainy"
    elif code in [71, 73, 75, 77, 85, 86]:
        return "Snowy"
    elif code in [95, 96, 99]:
        return "Thunderstorm"
    else:
        return "Unknown"


if __name__ == "__main__":
    main()
