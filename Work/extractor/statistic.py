# statistic
# Created by JKChang
# 2019-05-13, 10:03
# Tag:
# Description: method to extract metabolights statistic information

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import gspread
from oauth2client.service_account import  ServiceAccountCredentials

scope =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('../instance/metabolights-d3c2b1b419d0.json',scope)

gc = gspread.authorize(credentials)

wks = gc.open('MTBLS Curation Status Log').sheet1

print(wks.get_all_records())