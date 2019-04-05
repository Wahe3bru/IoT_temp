import pandas as pd
import numpy as np
import pygsheets
# from helper import open_worksheet2

def main():
    #from helper_dash.py
    def open_worksheet(spreadsheet_name, worksheet_title):
        client = pygsheets.authorize()
        sh = client.open(spreadsheet_name)
        wks = sh.worksheet_by_title(worksheet_title)
        return wks

    def worksheet_as_df(spreadsheet_name, worksheet_title):
        wks = open_worksheet(spreadsheet_name, worksheet_title)
        df = wks.get_as_df(empty_value=np.nan)
        return df

    spreadsheet_name ='unformat'

    client = pygsheets.authorize()

    df = worksheet_as_df('unformat','Sheet1')
    print('rows: ',len(df))
    # print('null rows: ',df.isnull().sum())
    df = df.dropna(how='all', axis=1)
    print('rows: ',len(df))
    df = df.dropna(how='all')
    print('dropping like its hot...')
    print('rows: ',len(df))

    sh = client.open(spreadsheet_name)
    wks2  = sh.add_worksheet('sheet2', rows=1, cols=1)
    wks2.set_dataframe(df, start='A1')
if __name__ == '__main__':
    main()
