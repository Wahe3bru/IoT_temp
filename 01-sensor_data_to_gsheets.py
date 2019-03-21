import datetime
import pygsheets
import Adafruit_DHT

client = pygsheets.authorize()

current_time = datetime.datetime.now()
month_year = current_time.strftime("%b-%Y")
month_year

# Open the spreadsheet and this months sheet .
sh = client.open('IoT_env')

try:
    wks = sh.worksheet_by_title(month_year)
except:
    wks = sh.add_worksheet(month_year, rows=0)
    wks.append_table(values=['timestamp', 'temperature', 'humidity'])

timestamp = current_time.strftime("%Y-%m-%d %H:%M")
humidity, temperature = Adafruit_DHT.read_retry(11, 17)
row = [timestamp, temperature, humidity]

# append row
wks.append_table(values=row)
