import requests
import os
from dotenv import load_dotenv
from datetime import datetime

from sms import send_sms

load_dotenv()

def is_umbrella_needed():
    parameters = {
        "lat": os.getenv("LATITUDE"),
        "lon": os.getenv("LONGITUDE"),
        "appid": os.getenv("WEATHER_API_KEY"),
        "units": "metric",
        "cnt": 6
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    forecast_data = response.json()['list']
    today = datetime.now().day
    for weather in forecast_data:
        time = datetime.fromtimestamp(int(weather['dt']))
        if time.day == today and time.hour < 22 and int(weather['weather'][0]['id']) < 700:
            return True, time.hour
    return False, None

    
umbrella, time = is_umbrella_needed()
if umbrella:
    send_sms(f"☔☔☔ Better have an umbrella, my dear, at {time}")
