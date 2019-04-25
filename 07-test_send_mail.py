from helper import send_email
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

gmail_username = os.environ['GMAIL_USERNAME']
gmail_password = os.environ['GMAIL_PASSWORD']

date= '25-04-2019'
temp_min, temp_mean, temp_max = 15, 16, 20
hum_min, hum_mean, hum_max =  34, 69, 88
log_counts = 123

send_email(
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
