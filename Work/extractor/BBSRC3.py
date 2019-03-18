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
print(len(df))

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

# df_split.to_csv('splited.tsv', sep='\t', encoding='utf-8', index=False)

df_split = df_split.drop_duplicates(subset=['MTBLS ID','Classify'],keep = 'last')
df_split.index = np.arange(1, len(df_split) + 1)

# tech_count = df_split['Classify'].value_counts(dropna=False)
# tech_count = tech_count.to_frame().reset_index()
# tech_count.columns = ['groupName', 'Count']
# tech_count.to_csv('counted.tsv', sep='\t', encoding='utf-8', index=False)

# count for NMR
tech = "NMR"
df_tech = df_split[df_split['Classify'] == tech]
df_tech.index = np.arange(1, len(df_tech) + 1)
print()



print()
