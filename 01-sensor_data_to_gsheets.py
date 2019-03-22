#! /usr/bin/python3

import datetime
import helper


def main():

    current_time = datetime.datetime.now()
    month_year = current_time.strftime("%b-%Y")

    timestamp = current_time.strftime("%Y-%m-%d %H:%M")
    humidity, temperature = helper.sensor_reading()
    row = [timestamp, temperature, humidity]

    columns = ['timestamp', 'temperature', 'humidity']
    wks = helper.open_worksheet('IoT_env', month_year, columns)
    # append row
    wks.append_table(values=row)


if __name__ == '__main__':

    main()
