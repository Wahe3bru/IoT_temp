import datetime
import pygsheets
import pandas as pd
import numpy as np
client = pygsheets.authorize()

current_time = datetime.datetime.now()
year = current_time.strftime("%Y")
date = current_time.strftime("%Y-%m-%d %H:%M")

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
sum_temp = 0
sum_hum = 0

# for row in wks:
#     if row[0].str.split(' ')[0] == date:
#         row_counts +=1
#         sum_temp += int(row[1])
#         sum_hum += int(row[2])
#
# print(sum_temp.min())
for row in wks:
    print(row_counts,': ',row[0])
