import datetime
import pygsheets
import pandas as pd
import numpy as np
client = pygsheets.authorize()

current_time = datetime.datetime.now()
year = current_time.strftime("%Y")
#date = current_time.strftime("%Y-%m-%d %H:%M")
date = "2019-03-02"

# Open the spreadsheet and this months sheet .
sh = client.open('2019-03_environmentals')
wks = sh.sheet1
# try:
#     wks = sh.worksheet_by_title(year)
# except:
#     wks = sh.add_worksheet(year, rows=0)
#     wks.append_table(values=['Date', 'Temperature-Min', 'Temperature-Mean',
#                              'Temperature-Max', 'Humidity'])

row_counts = 0
day_temp = []
day_hum = []

for row in wks:
    date_col = row[0]
    if date_col.split(' ')[0] == date:
        row_counts +=1
        day_temp.append(int(row[1]))
        # sum_hum += int(row[2])

print('min is ', np.min(day_temp))
print('average is ', np.mean(day_temp))
print('max is ', np.max(day_temp))
