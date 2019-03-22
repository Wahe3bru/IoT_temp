import datetime
import random


def get_sensor_reading():
    ''' replace with Adafruit_DHT.read_retry(11, 17)'''
    return (random.randint(19, 28), random.randint(60, 80))


def sensor_reading(attempts=5):
    '''returns the most common value from sensor reading'''
    readings = []
    for _ in range(attempts):
        readings.append(get_sensor_reading())
    humiditys, temperatures = zip(*readings)
    # find mode of readings
    humidity = max(set(humiditys), key=humiditys.count)
    temperature = max(set(temperatures), key=temperatures.count)
    return humidity, temperature


if __name__ == "__main__":

    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M")
    humidity, temperature = sensor_reading()
    row = [timestamp, temperature, humidity]
    row
