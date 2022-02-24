import pandas as pd
import httpx, time, math
from datetime import datetime

from weather_api.config import api_key

def weather_api_query(city: str, date: str, debug: bool = False) -> dict:
    # get lat and lon of city
    geocode = httpx.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}").json()

    if len(geocode) == 0:
        raise Exception("Error: city doesn't exist in database.")

    lat, lon = geocode[0]["lat"], geocode[0]["lon"]

    timestamp = math.floor(time.time())
    if date == "3 days ago":
        timestamp -= 24*3600*3
    elif date == "before yesterday":
        timestamp -= 24*3600*2
    elif date == "yesterday":
        timestamp -= 24*3600

    target = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&units=metric&dt={timestamp}&appid={api_key}"
    data = httpx.get(target).json()

    weather_data_structure = pd.DataFrame()
    # history weather data
    for d in data["hourly"]:
        weather_data_structure = pd.concat([weather_data_structure, pd.DataFrame({
        "City": [city],
        "Time": [datetime.fromtimestamp(d["dt"])],
        "Weather Main": [d["weather"][0]["main"]],
        "Weather Description": [d["weather"][0]["description"]],
        "Weather Icon ID": [d["weather"][0]["icon"]],
        "Temperature": [d["temp"]],
        "Temperature Felt": [d["feels_like"]],
        "Pressure" : [d["pressure"]],
        "Humidity": [d["humidity"]],
        "Wind Speed": [d["wind_speed"]]
    })], ignore_index=True)

    if date == "today":
        # current weather data
        weather_data_structure = pd.concat([weather_data_structure, pd.DataFrame({
            "City": [city],
            "Time": [datetime.fromtimestamp(data["current"]["dt"])],
            "Weather Main": [data["current"]["weather"][0]["main"]],
            "Weather Description": [data["current"]["weather"][0]["description"]],
            "Weather Icon ID": [data["current"]["weather"][0]["icon"]],
            "Temperature": [data["current"]["temp"]],
            "Temperature Felt": [data["current"]["feels_like"]],
            "Pressure" : [data["current"]["pressure"]],
            "Humidity": [data["current"]["humidity"]],
            "Wind Speed": [data["current"]["wind_speed"]]
        })], ignore_index=True)

    if debug:
        print(f"\n[DEBUG] << {datetime.now().strftime('%H:%M:%S')} >>")
        print(f"URL={target}\n")
        print(weather_data_structure)

    return weather_data_structure