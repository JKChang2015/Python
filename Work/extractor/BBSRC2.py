# BBSRC2
# Created by JKChang
# 2019-03-13, 12:22
# Tag:
# Description: 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from Work.extractor import fileReader, studyList

studyIDs = studyList.getStudyIDs(publicStudy=True)

df = pd.read_csv('../resources/MTBLS Curation Status Log.tsv',sep='\t')
df = df[df['Status'].isin (['Public','In Review' ])]
df = df[['MTBLS ID', 'Study Type']]

# df.to_csv('techniques.tsv', sep='\t', encoding='utf-8', index=False)

df_split = pd.DataFrame(columns=['MTBLS ID', 'Study Type'])

for index, row in df.iterrows():
    try:
        temp = row.copy()
        techniques = row['Study Type'].split(';')
        for technique in techniques:
            temp['Study Type'] = technique
            df_split.loc[len(df_split)] = temp
    except:
        df_split.loc[len(df_split)] = row

# NMR_studies = df_split[df_split['Study Type'].isin(['NMR','MAS-NMR'])]['MTBLS ID'].tolist()
# print(len(set(NMR_studies)))
# print()

# df_split.to_csv('splited.tsv', sep='\t', encoding='utf-8', index=False)

# list of mulit tech studies
# multi = df_split[df_split['MTBLS ID'].isin(df_split['MTBLS ID'].value_counts()[df_split['MTBLS ID'].value_counts()>1].index)]
# res = sorted(multi['MTBLS ID'].tolist())
# print(set(res))
# print(len(set(res)))

# count the Techniques
df_count = df_split['Study Type'].value_counts(dropna=False)
df_count = df_count.to_frame().reset_index()
df_count.columns = ['Technique', 'Count']

# load full name of the techniques
names = pd.read_csv('../resources/full name.csv')
name_pair = dict(zip(names['Study type'], names['Full Name']))
df_count['Full Name'] = df_count['Technique'].map(name_pair)
# df_count.to_csv('counted.tsv', sep='\t', encoding='utf-8', index=False)

# group count
group = dict(zip(names['Study type'], names['Classify']))
temp = df_split['Study Type'].map(group, na_action=None)

# temp.to_csv('grouped.tsv', sep='\t', encoding='utf-8', index=False)

df_group = temp.value_counts(dropna=False)
df_group = df_group.to_frame().reset_index()
df_group.columns = ['groupName', 'Count']
df_group.to_csv('group count.tsv', sep='\t', encoding='utf-8', index=False)
#
# print()

