# google_sheet
# Created by JKChang
# 16/09/2019, 11:04
# Tag:
# Description:


import gspread
import pandas as pd
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials


def setGoogleSheet(df, url, worksheetName):
    '''
    set whole dataframe to google sheet, if sheet existed create a new one
    :param df: dataframe want to save to google sheet
    :param url: url of google sheet
    :param worksheetName: worksheet name
    :return: Nan
    '''
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('../instance/metabolights-d3c2b1b419d0.json', scope)
    gc = gspread.authorize(credentials)
    try:
        wks = gc.open_by_url(url).worksheet(worksheetName)
        print(worksheetName + ' existed... create a new one')
        wks = gc.open_by_url(url).add_worksheet(title=worksheetName + '_1', rows=df.shape[0], cols=df.shape[1])
    except:
        wks = gc.open_by_url(url).add_worksheet(title=worksheetName, rows=df.shape[0], cols=df.shape[1])
    set_with_dataframe(wks, df)


def getGoogleSheet(url, worksheetName):
    '''
    get google sheet
    :param url: url of google sheet
    :param worksheetName: work sheet name
    :return: data frame
    '''
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('../instance/metabolights-d3c2b1b419d0.json', scope)
    gc = gspread.authorize(credentials)
    # wks = gc.open('Zooma terms').worksheet('temp')
    wks = gc.open_by_url(url).worksheet(worksheetName)
    content = wks.get_all_records()
    # max_rows = len(wks.get_all_values())
    df = pd.DataFrame(content)
    return df


def replaceGoogleSheet(df, url, worksheetName):
    '''
    replace the old google sheet with new data frame, old sheet will be clear
    :param df: dataframe
    :param url: url of google sheet
    :param worksheetName: work sheet name
    :return: Nan
    '''
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('../instance/metabolights-d3c2b1b419d0.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_url(url).worksheet(worksheetName)
    wks.clear()
    set_with_dataframe(wks, df)


import numpy as np

df = pd.DataFrame(np.arange(12).reshape(4, 3))
setGoogleSheet(df,
               'https://docs.google.com/spreadsheets/d/1lecrjeJj8M6GXPUUZaK0KRvcVDYJzdI_Y1S9TwkYvSU/edit#gid=820103365',
               'temp')

d = getGoogleSheet(
    'https://docs.google.com/spreadsheets/d/1lecrjeJj8M6GXPUUZaK0KRvcVDYJzdI_Y1S9TwkYvSU/edit#gid=820103365', 'temp')
d.drop_duplicates(subset=['studyID', 'name'], inplace=True)
d.dropna(subset=['studyID', 'name'])

replaceGoogleSheet(d,
                   'https://docs.google.com/spreadsheets/d/1lecrjeJj8M6GXPUUZaK0KRvcVDYJzdI_Y1S9TwkYvSU/edit#gid=820103365',
                   'temp')

print()
