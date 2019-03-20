import datetime
import pygsheets
import numpy as np

client = pygsheets.authorize()

current_time = datetime.datetime.now()
date = current_time.strftime("%Y-%m-%d")
month_year = current_time.strftime("%b-%Y")
year = current_time.strftime("%Y")

# Open the spreadsheet and this months sheet .
sh = client.open('IoT_env')
try:
    wks = sh.worksheet_by_title(month_year)
except:
    wks = sh.add_worksheet(month_year, rows=0)
    wks.append_table(values=['timestamp', 'temperature', 'humidity'])


row_counts = 0
day_temp = []
day_hum = []

for row in wks:
    date_col = row[0]
    if date_col.split(' ')[0] == date: #is this best way to filter date?
        row_counts +=1
        day_temp.append(int(row[1]))
        day_hum.append(int(row[1]))

# do i create vars below, or plug them directory into day_stats_row list??
temp_min =  str(np.min(day_temp))
temp_mean = str(np.mean(day_temp))
temp_max = str(np.max(day_temp))

hum_min =  str(np.min(day_hum))
hum_mean = str(np.mean(day_hum))
hum_max = str(np.max(day_hum))

day_stats_row = [date, temp_min, temp_mean, temp_max, hum_min, hum_mean, hum_max]

sh_write = client.open('daily_stats')
try:
    wks_write = sh_write.worksheet_by_title(year)
except:
    wks_write = sh_write.add_worksheet(year, rows=0)
    wks_write.append_table(values=['Date', 'Temperature-Min', 'Temperature-Mean',
                             'Temperature-Max', 'Humidity-Min', 'Humidity-Mean',
                             'Humidity-Max',])

wks_write.append_table(values=day_stats_row)

# possible enhancements
# add summary of month, streaks (hottest, coldest, etc)
# add weather condition sourced from weather api
