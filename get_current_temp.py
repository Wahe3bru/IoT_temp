""" """
import datetime
import Adafruit_DHT

timestamp = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

humidity, temperature = Adafruit_DHT.read_retry(11, 17)
print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
