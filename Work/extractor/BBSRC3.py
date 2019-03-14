# BBSRC3
# Created by JKChang
# 2019-03-14, 09:16
# Tag:
# Description: 

import pandas as pd
import numpy as np
from Work.extractor import fileReader,studyList

df = pd.read_csv('../resources/MTBLS Curation Status Log.tsv',sep='\t')

# for public/ in review only
df = df[df['Status'].isin (['Public','In Review' ])]
df = df[['MTBLS ID', 'Study Type']]

# split the techniques into different lines
df_split = pd.DataFrame(columns=['MTBLS ID', 'Study Type','Full name','Classify'])

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
name_pair = dict(zip(full_names['Study type'],full_names['Full Name']))
classify_pair = dict(zip(full_names['Study type'],full_names['Classify']))
df_split['Full name'] = df_split['Study Type'].map(name_pair)
df_split['Classify'] = df_split['Study Type'].map(classify_pair)

df_split.to_csv('splited.tsv', sep='\t', encoding='utf-8', index=False)