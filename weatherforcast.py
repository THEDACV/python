import requests
import json

# Replace with your OpenWeatherMap API key
api_key = "YOUR_API_KEY"

# City name (replace with your desired location)
city_name = "London"

# Base URL for the API request
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Complete URL with API key, city name, and units (metric by default)
complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"

try:
  # Send HTTP GET request
  response = requests.get(complete_url)
  response.raise_for_status()  # Raise an exception for non-200 status codes
except requests.exceptions.RequestException as e:
  print(f"Error retrieving weather data: {e}")
  exit()

# Parse JSON response
data = json.loads(response.text)

# Extract weather description
weather_description = data["weather"][0]["description"]

# Extract temperature (in Kelvin)
temperature_kelvin = data["main"]["temp"]
temperature_celsius = round(temperature_kelvin - 273.15, 2)  # Convert to Celsius

# Extract humidity
humidity = data["main"]["humidity"]

# Display weather information
print(f"Weather in {city_name}:")
print(f"\tDescription: {weather_description}")
print(f"\tTemperature: {temperature_celsius:.2f} °C")
print(f"\tHumidity: {humidity}%")
