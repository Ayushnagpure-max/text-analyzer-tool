import os
import requests

print("WEATHER FORECAST COMMAND-LINE APP")
print("-" * 35)

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    print("Error: API key not found.")
    exit()

city = input("Enter city name: ").strip()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if response.status_code != 200:
        print("Error:", data.get("message", "Unable to fetch weather data"))
        exit()

except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")
    exit()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
condition = data["weather"][0]["description"]

print("\nWeather Report for:", city)
print("-" * 30)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Wind Speed:", wind_speed, "m/s")
print("Condition:", condition.capitalize())
