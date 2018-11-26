# reMapping
# Created by JKChang
# 2018-11-26, 14:14
# Tag:
# Description: 

import pandas as pd

df = pd.read_csv('metabolights_zooma 3.tsv', sep='\t', encoding='utf-8')

df_res = pd.DataFrame(columns=['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG',
                               'ANNOTATOR', 'ANNOTATION_DATE'])

for index, row in df.iterrows():
    temp = row.copy()
    studies = row['STUDY'].split(',')
    for study in studies:
        temp['STUDY'] = study
        df_res.loc[len(df_res)] = temp

df_res.to_csv('splited.tsv', sep='\t', encoding='utf-8', index=False)
