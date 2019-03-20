import datetime
import pygsheets
import pandas as pd

client = pygsheets.authorize()

current_time = datetime.datetime.now()
year = current_time.strftime("%Y")
date = current_time.strftime("%Y-%m-%d %H:%M")

# Open the spreadsheet and this months sheet .
sh = client.open('daily_stats')

try:
    wks = sh.worksheet_by_title(year)
except:
    wks = sh.add_worksheet(year, rows=0)
    wks.append_table(values=['Date', 'Temperature-Min', 'Temperature-Mean', 'Temperature-Max', 'Humidity'])
