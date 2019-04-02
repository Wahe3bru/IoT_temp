from os.path import join, dirname
from dotenv import load_dotenv
import pygsheets

def main():
    spreadsheet_name ='IoT_env'

    client = pygsheets.authorize()

    def get_worksheet_titles(spreadsheet_name):
        sh = client.open(spreadsheet_name)
        worksheet_titles = sh.worksheets()
        wks_titles = []
        for title in worksheet_titles:
            wks_titles.append(str(title).split("'")[1])
        return wks_titles

    print(get_worksheet_titles(spreadsheet_name))
if __name__ == '__main__':
    main()
