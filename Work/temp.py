# temp
# Created by JKChang
# 2018-11-27, 11:20
# Tag:
# Description:  split list of study into different rows

import pandas as pd
import numpy as np

import json
from owlready2 import urllib



def getStudyID(query, attribute):

    if attribute == 'factor':
        filename = './resources/study factors.tsv'
    elif attribute == 'organism':
        filename = './resources/study organism.tsv'
    elif attribute == 'organismPart':
        filename = './resources/study organismPart.tsv'
    else:
        filename = ''

    try:
        df = pd.read_csv(filename,sep='\t', encoding='utf-8')
        df = df.replace(np.nan,'',regex=True)

        try:
            temp = df[df[attribute].str.contains(query,case= False)]
            return list(temp['studyID'].unique())
        except:
            pass
    except:
        print('invalid file name')


metabo_zooma = pd.read_csv('./resources/metabolights_zooma test.tsv', sep='\t')
metabo_zooma = metabo_zooma.replace(np.nan, '', regex=True)

df_res = pd.DataFrame(columns=['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG',
                               'ANNOTATOR', 'ANNOTATION_DATE'])


attribute = 'organismPart'

for index,row in metabo_zooma.iterrows():
    query = row['PROPERTY_VALUE']
    temp = row.copy()
    if getStudyID(query, attribute) is not None and len(getStudyID(query, attribute)) > 0:
        studyIDs = getStudyID(query,attribute)
        for studyID in studyIDs:
            temp['STUDY'] = studyID
            temp['PROPERTY_TYPE'] = attribute
    else:
        pass

df_res.to_csv('test res.tsv',sep='\t',encoding='utf-8',index= False)



# df = pd.read_csv('metabolights_zooma test.tsv', sep='\t', encoding='utf-8')
#
# df_res = pd.DataFrame(columns=['STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG',
#                                'ANNOTATOR', 'ANNOTATION_DATE'])
#
# for index, row in df.iterrows():
#     temp = row.copy()
#     studies = row['STUDY'].split(',')
#     for study in studies:
#         temp['STUDY'] = study
#         df_res.loc[len(df_res)] = temp
#
# df_res.to_csv('splited.tsv', sep='\t', encoding='utf-8', index=False)
