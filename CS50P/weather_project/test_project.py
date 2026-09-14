from unittest.mock import Mock, patch

from project import describe_weather, get_location, get_weather


def test_get_location():
    fake_response = Mock()
    fake_response.read.return_value = b'''{
        "results": [
            {
                "name": "Tehran",
                "country": "Iran",
                "latitude": 35.69,
                "longitude": 51.42
            }
        ]
    }'''

    with patch("project.urlopen", return_value=fake_response):
        result = get_location("Tehran")

    assert result["name"] == "Tehran"
    assert result["latitude"] == 35.69


def test_get_weather():
    fake_response = Mock()
    fake_response.read.return_value = b'''{
        "current": {
            "temperature_2m": 25,
            "wind_speed_10m": 10,
            "weather_code": 0
        }
    }'''

    with patch("project.urlopen", return_value=fake_response):
        result = get_weather(35.69, 51.42)

    assert result["temperature"] == 25
    assert result["wind_speed"] == 10


def test_describe_weather():
    assert describe_weather(0) == "Clear sky"
    assert describe_weather(3) == "Cloudy"
    assert describe_weather(61) == "Rainy"
    assert describe_weather(95) == "Thunderstorm"
