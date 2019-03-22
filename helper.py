from os.path import join, dirname
from dotenv import load_dotenv
import pygsheets
import Adafruit_DHT


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def open_worksheet(spreadsheet_name, worksheet_title, col_names):
    """Open spreadsheet and worksheet, creating worksheet with column headers
    if it doesn't exist.

    Args:
        spreadsheet_name (str): Name of Spreadsheet document. Has to exist atm.
        worksheet_title (str): Name of worksheet within spreadsheet.
        col_names (list): list of column names
    Returns:
        wks: a pygsheets.worksheet object

    """
    client = pygsheets.authorize()
    sh = client.open(spreadsheet_name)
    try:
        wks = sh.worksheet_by_title(worksheet_title)
    except:
        wks = sh.add_worksheet(worksheet_title, rows=0)
        wks.append_table(values=col_names)

    return wks


def sensor_reading(attempts=5):
    '''returns the most common value from sensor reading'''
    readings = []
    for _ in range(attempts):
        readings.append(Adafruit_DHT.read_retry(11, 17))
    humiditys, temperatures = zip(*readings)
    # find mode of readings
    humidity = max(set(humiditys), key=humiditys.count)
    temperature = max(set(temperatures), key=temperatures.count)
    return humidity, temperature


def main():
    # testing
    columns = ['timestamp', 'col1', 'name']
    wks = open_worksheet('2019-03_environmentals', 'test1', columns)
    wks.append_table(values=['now', '123434', 'wally'])


if __name__ == '__main__':
    main()
