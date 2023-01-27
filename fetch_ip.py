import requests
import json
import config

def get_ip():
    # fetch api
    URL = "https://geo.ipify.org/api/v2/country,city?"
    params = {
        'apiKey': config.IP_API_KEY
    }

    response = requests.get(URL, params=params)
    data = response.text
    parse_json = json.loads(data)
    user_location = parse_json['location']['city']

    print(user_location)

    return user_location