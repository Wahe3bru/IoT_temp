#! /usr/bin/python3

import datetime
import helper
import numpy as np
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

gmail_username = os.environ['GMAIL_USERNAME']
gmail_password = os.environ['GMAIL_PASSWORD']

def main():

    current_time = datetime.datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    month_year = current_time.strftime("%b-%Y")
    year = current_time.strftime("%Y")

    # Open the spreadsheet and this months sheet .
    columns = ['timestamp', 'fix me']
    wks = helper.open_worksheet('IoT_env', month_year, columns)

    row_counts = 0
    day_temp = []
    day_hum = []

    for row in wks:
        date_col = row[0]
        if date_col.split(' ')[0] == date:  # is this best way to filter date?
            row_counts += 1
            day_temp.append(int(row[1]))
            day_hum.append(int(row[2]))

    # do i create vars below, or plug them directory into day_stats_row list??
    temp_min = str(np.min(day_temp))
    temp_mean = str(np.mean(day_temp))
    temp_max = str(np.max(day_temp))

    hum_min = str(np.min(day_hum))
    hum_mean = str(np.mean(day_hum))
    hum_max = str(np.max(day_hum))
    log_counts = str(row_counts)

    day_stats_row = [date, temp_min, temp_mean, temp_max, hum_min, hum_mean,
                     hum_max, log_counts]

    columns = ['Date', 'Temperature-Min', 'Temperature-Mean', 'Temperature-Max',
               'Humidity-Min', 'Humidity-Mean', 'Humidity-Max', '#Records']
    wks_write = helper.open_worksheet('daily_stats', year, columns)
    wks_write.append_table(values=day_stats_row)

    helper.send_email(
        username=gmail_username,
        password=gmail_password,
        recipient='wahe3b@gmail.com',
        subject='Environment Summary for {}'.format(date),
        body='''Environment summary
        Temperature:
          min: {temp_min}
          average: {temp_mean}
          max: {temp_max}

        Humidity:
          min: {hum_min}
          average: {hum_mean}
          max: {hum_max}

        logged {log_counts} times.'''.format(temp_min=temp_min, temp_mean=temp_mean,
         temp_max=temp_max, hum_min=hum_min, hum_mean=hum_mean, hum_max=hum_max,
         log_counts=log_counts),
        )


if __name__ == '__main__':

    main()
# possible enhancements
# add summary of month, streaks (hottest, coldest, etc)
# add weather condition sourced from weather api
