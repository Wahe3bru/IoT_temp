
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import datetime
import pygsheets

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
api_key = os.getenv('OWMapi_key')

OWMapi_key = api_key
cape_town_id = '&id=3370352'
city_name = "&q=Cape Town"
metric_units = "&units=metric"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid="
api_call = BASE_URL + OWMapi_key + city_name + metric_units

weather_data = requests.get(api_call).json()
temperature = weather_data['main']['temp']
humidity = weather_data['main']["humidity"]
pressure  = weather_data['main']['pressure']
description = weather_data['weather'][0]['description']

current_time = datetime.datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M")
month_year = current_time.strftime("%b-%Y")

client = pygsheets.authorize()
# Open the spreadsheet and this months sheet .
sh = client.open('Outside_env')

try:
    wks = sh.worksheet_by_title(month_year)
except:
    wks = sh.add_worksheet(month_year, rows=0)
    wks.append_table(values=['timestamp', 'temperature', 'humidity', 'description'])


row = [timestamp, temperature, humidity, description]

# append row
wks.append_table(values=row)
