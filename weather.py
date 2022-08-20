from urllib import response
import requests

API_KEY = "get_key_from_site"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Query parameters
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Current weather for {city.capitalize()}: {weather}")
    temperature = round((data['main']['temp'] - 273.15) * (9/5) + 32, 2)
    print(f"Current temperature: {temperature}°F")
else:
    print("An error occurred.")