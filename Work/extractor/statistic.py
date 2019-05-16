# statistic
# Created by JKChang
# 2019-05-13, 10:03
# Tag:
# Description: method to extract Metabolights statistic information

import gspread
import numpy as np
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Load spreadsheet from Google sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('../instance/metabolights-a804a09729cc.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('MTBLS Curation Status Log').sheet1
content = wks.get_all_records()

df = pd.DataFrame(content)

#  Public study only
df = df[df['Status'] == 'Public']

#  Public and In-review study only
# df = df[df['Status'].isin(['Public','In Review'])]

df = df[['MTBLS ID', 'Study Type']]
df['Study Type'].replace('', np.nan, inplace=True)
df = df.dropna(subset=['Study Type'])

# split the techniques into different lines
df_split = pd.DataFrame(columns=['MTBLS ID', 'Study Type', 'Full name', 'Classify'])

for index, row in df.iterrows():
    try:
        temp = row.copy()
        techniques = row['Study Type'].split(';')
        for technique in techniques:
            temp['Study Type'] = technique
            df_split.loc[len(df_split)] = temp
    except:
        df_split.loc[len(df_split)] = row

# map full name and classify to each line
full_names = pd.read_csv('../resources/full name.csv')
name_pair = dict(zip(full_names['Study type'], full_names['Full Name']))
classify_pair = dict(zip(full_names['Study type'], full_names['Classify']))
df_split['Full name'] = df_split['Study Type'].map(name_pair)
df_split['Classify'] = df_split['Study Type'].map(classify_pair)

df_split = df_split.drop_duplicates(subset=['MTBLS ID', 'Classify'], keep='last')
df_split.index = np.arange(1, len(df_split) + 1)

# Count in group

tech_count = df_split['Classify'].value_counts(dropna=False)
tech_count = tech_count.to_frame().reset_index()
tech_count.columns = ['groupName', 'Count']


def top(df, col_name, num):
    temp = df.sort_values(by=col_name, ascending=False)
    res = temp.nlargest(num, col_name)
    t = temp[num:]['Count'].sum()
    res.loc[len(res)] = ['Others', t]
    return res

res = top(tech_count, 'Count', 4)

print()
