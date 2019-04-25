from os.path import join, dirname
from dotenv import load_dotenv
import pygsheets
import Adafruit_DHT
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from pathlib import Path

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def open_worksheet(spreadsheet_name, worksheet_title, col_names):
    """Open spreadsheet and worksheet, creating worksheet with column headers
    if it doesn't exist.

    Args:
        spreadsheet_name (str): Name of Spreadsheet document. Has to exist atm.
        worksheet_title (str):  Name of worksheet within spreadsheet.
        col_names (list):       list of column names
    Returns:
        wks: a pygsheets.worksheet object

    """
    client = pygsheets.authorize()
    sh = client.open(spreadsheet_name)
    try:
        wks = sh.worksheet_by_title(worksheet_title)
    except:
        wks = sh.add_worksheet(worksheet_title, rows=1, cols=1)
        wks.append_table(values=col_names)

    return wks


def sensor_reading(attempts=5):
    '''returns the most common value from sensor reading

       args:
           attempts (int): number of readings to take
       return:
           tuple: containing value of humidity and temperature
    '''
    readings = []
    for _ in range(attempts):
        readings.append(Adafruit_DHT.read_retry(11, 17))
    humiditys, temperatures = zip(*readings)
    # find mode of readings
    humidity = max(set(humiditys), key=humiditys.count)
    temperature = max(set(temperatures), key=temperatures.count)
    return humidity, temperature

def send_email(username, password, recipient, subject, body):
    """Send email via Gmail

    :param username: Gmail username that is also used in the "From" field
        e.g. pyderpuffgirls@gmail.com
    :param password: Gmail password
    :param recipient: a string or list of the email address of recipient(s)
    :param subject: the subject of email
    :param body: the body of email
    """

    smtp_server = "smtp.gmail.com"
    port = 465
    ssl_context = ssl.create_default_context()

    # https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
    if isinstance(recipient, str):
        recipient = [recipient]
    recipients_string = ', '.join(recipient)  # e.g. "person1@gmail.com, person2@gmail.com"

    # create email
    email = MIMEMultipart()

    # Add body, then set the email metadata
    if body is not None:
        content = MIMEText(body)
        email.attach(content)

    email['Subject'] = subject
    email['From'] = username
    email['To'] = recipients_string

    with smtplib.SMTP_SSL(smtp_server, port, context=ssl_context) as conn:
        conn.login(username, password)
        conn.sendmail(username, recipient, email.as_string())
    pass

def main():
    # testing
    columns = ['timestamp', 'col1', 'name']
    wks = open_worksheet('2019-03_environmentals', 'test1', columns)
    wks.append_table(values=['now', '123434', 'wally'])


if __name__ == '__main__':
    main()
