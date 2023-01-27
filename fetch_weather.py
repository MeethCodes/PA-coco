# FETCH WEATHER USING IP LOCATION

import fetch_ip
import json
import requests
import config

user_location = fetch_ip.get_ip()
URL = "https://api.openweathermap.org/data/2.5/weather?"
params = {
    'q': user_location,
    'appid': config.WEATHER_API_KEY,
    'units': 'metric'
}

def fetch_weather():
    response = requests.get(URL, params=params)
    data = response.text
    parse_json = json.loads(data)
    main = parse_json['weather'][0]['description']
    temp = parse_json['main']['temp']

    return main, temp