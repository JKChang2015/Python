# metabolights_zooma
# Created by JKChang
# 2018-11-23, 09:44
# Tag:
# Description: mapping metabolights terms with study information

import pandas as pd
import numpy as np

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

metabo_zooma = pd.read_csv('./resources/metabolights_zooma.tsv', sep='\t')
metabo_zooma = metabo_zooma.replace(np.nan, '', regex=True)
# 'STUDY', 'BIOENTITY', 'PROPERTY_TYPE', 'PROPERTY_VALUE', 'SEMANTIC_TAG','ANNOTATOR', 'ANNOTATION_DATE'

# 'studyID', 'factor'

attribute = 'factor'


for index, row in metabo_zooma.iterrows():
    query = row['PROPERTY_VALUE']
    if getStudyID(query,attribute) is not None and len(getStudyID(query,attribute)) >0:
        row['STUDY'] = ','.join(getStudyID(query,attribute))
        row['PROPERTY_TYPE'] = attribute
    else:
        pass

    print(query)

metabo_zooma.to_csv('./resources/metabolights_zooma.tsv',sep='\t',encoding='utf-8',index=False)



