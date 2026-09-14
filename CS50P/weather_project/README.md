# Simple Weather Program

#### Video Demo: <https://youtu.be/UA_hV2ixjFU>

#### Description:

Simple Weather Program is a beginner command-line project written in Python.
The purpose of this project is to let the user check the current weather of a
city. The user types the name of a city, and the program shows the city and
country, current temperature, wind speed, and a simple description of the
weather. For example, the condition may be clear, cloudy, rainy, snowy, foggy,
or a thunderstorm.

The program gets its information from Open-Meteo. I chose Open-Meteo because it
provides weather and location information without requiring an API key for this
simple project. This makes the program easier to install and use. An internet
connection is still required when running the main program because the weather
information is received online.

The project contains four files. The first file is `project.py`, which contains
the main program. The second file is `test_project.py`, which contains the tests
for the functions. The third file is `requirements.txt`, which lists pytest as
a required installable package. The fourth file is this `README.md`, which
explains the project and how to use it.

The `main` function is the starting point of the program. It displays the title
and asks the user to enter a city name. If the user enters an empty value, the
program prints an error message and stops. Otherwise, `main` calls the other
functions and prints the final weather result. It also handles common internet
or API errors and shows a simple message instead of crashing.

The `get_location` function receives the city name. It sends that name to the
Open-Meteo Geocoding API. The API returns location data, including latitude and
longitude. The function uses the first matching result and returns the city
name, country, latitude, and longitude in a Python dictionary. If the city is
not found, it returns `None`.

The `get_weather` function receives latitude and longitude. It uses these two
values to request the current weather from the Open-Meteo Forecast API. It then
returns the temperature, wind speed, and numeric weather code in another
dictionary. Separating location search and weather search into two functions
makes the code easier to read and test.

The `describe_weather` function changes a numeric weather code into a short
description. A user may not understand a code such as 0, 61, or 95. This
function uses simple `if` and `elif` conditions to return understandable text.
For example, code 0 returns "Clear sky," rain codes return "Rainy," and storm
codes return "Thunderstorm."

The `test_project.py` file contains three test functions:
`test_get_location`, `test_get_weather`, and `test_describe_weather`. The first
two tests use fake API responses. Because of this, the tests do not need a real
internet connection and do not change when the real weather changes. The last
test checks several weather codes and their expected descriptions.

I decided to build a command-line program instead of a graphical application
because I wanted the project to remain simple and focused on Python functions,
APIs, dictionaries, conditions, and testing. A future version could display
humidity, daily forecasts, or save favorite cities, but the current version
focuses on providing a clear and useful current-weather result.

To install the test dependency, run:

```bash
pip install -r requirements.txt
```

To start the program, run:

```bash
python project.py
```

To run all tests, use:

```bash
pytest
```
