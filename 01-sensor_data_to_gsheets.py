#! /usr/bin/python3

import datetime
import Adafruit_DHT
import helper

def main():
    current_time = datetime.datetime.now()
    month_year = current_time.strftime("%b-%Y")

    timestamp = current_time.strftime("%Y-%m-%d %H:%M")
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    row = [timestamp, temperature, humidity]

    columns = ['timestamp', 'temperature', 'humidity']
    wks = helper.open_worksheet('IoT_env', month_year, columns)
    # append row
    wks.append_table(values=row)

if __name__ == '__main__':
    main()
