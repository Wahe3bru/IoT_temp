
import requests
import helper
import datetime
import pygsheets
import os
def create_OWM_api_call(OWMapi_key, city_id='&id=3370352',
                        city_name="&q=Cape Town", use_id=False):
    ''' '''
    metric_units="&units=metric"
    BASE_URL="http://api.openweathermap.org/data/2.5/weather?appid="
    if use_id:
        api_call = BASE_URL + OWMapi_key + city_id + metric_units
    else:
        api_call = BASE_URL + OWMapi_key + city_name + metric_units
    return api_call

def get_weather_from_OWM(api_call):
    weather_data = requests.get(api_call).json()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']["humidity"]
    pressure  = weather_data['main']['pressure']
    description = weather_data['weather'][0]['description']
    return [humidity, temperature, pressure, description]

def main():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M")
    month_year = current_time.strftime("%b-%Y")

    client = pygsheets.authorize()
    sh = client.open('Outside_env')
    try:
        wks = sh.worksheet_by_title(month_year)
    except:
        wks = sh.add_worksheet(month_year, rows=0)
        wks.append_table(values=['timestamp', 'temperature', 'humidity', 'pressure', 'description'])

    api_key = os.getenv('OWMapi_key')
    api_call = create_OWM_api_call(api_key)
    outside_env = get_weather_from_OWM(api_call)

    row = [timestamp] + outside_env

    # append row
    wks.append_table(values=row)

if __name__ == '__main__':
    main()
