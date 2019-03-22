
import requests

# save to .env
OWMapi_key = 'a0c5d96f0c8578371ab236a9a42821d2'
cape_town_id = '&id=3370352'
name = "&q=Cape Town"
metric_units = "&units=metric"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
api_call = BASE_URL + OWMapi_key + name + metric_units
api_call
http://api.openweathermap.org/data/2.5/weather?appid=a0c5d96f0c8578371ab236a9a42821d2&q=Cape%20Town&units=metric
weather_data = requests.get(api_call).json()
temp = weather_data['main']['temp']
humidity = weather_data['main']["humidity"]
pressure  = weather_data['main']['pressure']
description = weather_data['weather']['description']

print(f'{temp}*C  {humidity}% ')
