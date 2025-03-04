# Description: This file contains the code for the weather sensor that fetches weather data from the OpenWeatherMap API.
import datetime
import requests

# OpenWeatherMap API key:
API_KEY = "6c75ff9290b80b9ee9641bef1f53fd0b"


def fetch_weather_alerts(city="San Francisco"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        # If temperature exceeds 30°C, trigger an alert; otherwise, return a regular weather update.
        if temp > 30:
            title = "Heat Alert"
            description = f"High temperature of {temp}°C in {city}."
            status = "alert"
        else:
            title = "Weather Update"
            description = f"Temperature in {city} is {temp}°C."
            status = "normal"
            
        incident_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        
        incident = {
            "title": title,
            "description": description,
            "incident_time": incident_time,
            "latitude": lat,
            "longitude": lon,
            "status": status
        }
        return incident
    else:
        # Log error details for debugging
        print(f"Error fetching weather data: {response.status_code} - {response.text}")
        return None