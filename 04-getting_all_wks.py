from os.path import join, dirname
from dotenv import load_dotenv
import pandas as pd
import pygsheets

def main():
    #from helper_dash.py
    def open_worksheet(spreadsheet_name, worksheet_title):
        client = pygsheets.authorize()
        sh = client.open(spreadsheet_name)
        wks = sh.worksheet_by_title(worksheet_title)
        return wks

    def worksheet_as_df(spreadsheet_name, worksheet_title):
        wks = open_worksheet(spreadsheet_name, worksheet_title)
        df = wks.get_as_df()
        return df

    spreadsheet_name ='IoT_env'

    client = pygsheets.authorize()

    def get_worksheet_titles(spreadsheet_name):
        sh = client.open(spreadsheet_name)
        worksheet_titles = sh.worksheets()
        return [str(title).split("'")[1] for title in worksheet_titles]

    worksheets = get_worksheet_titles(spreadsheet_name)

    all_df = pd.DataFrame()
    for title in worksheets:
         df = worksheet_as_df(spreadsheet_name,title)
         print(title, len(df))
         all_df = all_df.append(df)

    # need to create one big df
    print('all data: ', len(all_df))
if __name__ == '__main__':
    main()
