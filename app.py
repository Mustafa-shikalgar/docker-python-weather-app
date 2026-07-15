import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\n========== Weather Report ==========")
    print(f"City        : {data['name']}")
    print(f"Country     : {data['sys']['country']}")
    print(f"Temperature : {data['main']['temp']} °C")
    print(f"Feels Like  : {data['main']['feels_like']} °C")
    print(f"Humidity    : {data['main']['humidity']} %")
    print(f"Weather     : {data['weather'][0]['description'].title()}")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")
    print("====================================")
    
else:
    print("City not found or invalid API key.")
