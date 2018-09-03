# zooma
# Created by JKChang
# 09/08/2018, 14:57
# Tag:
# Description: 

import json
import urllib.request

import pandas as pd


def getSemanticTag(keyword):
    try:
        url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue=' + keyword.replace(' ', "+")
        fp = urllib.request.urlopen(url)
        content = fp.read()
        json_str = json.loads(content)[0]
        return json_str['semanticTags']
    except:
        return ''


def getConfidence(keyword):
    # only return the first suggestion term, need to be fix
    try:
        url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue=' + keyword.replace(' ', "+")
        fp = urllib.request.urlopen(url)
        content = fp.read()
        json_str = json.loads(content)[0]
        return json_str['confidence']
    except:
        return ''


df = pd.read_table(r'/Users/jkchang/test/factors.tsv', sep='\t')
res = []
for row in range(df.shape[0]):
    rowData = df.iloc[row]
    try:
        terms = [x.title() for x in rowData['terms'].split(',')]
        for term in set(terms):
            res.append([rowData['StudyID'], term])
    except:
        pass

new = pd.DataFrame(res, columns=['StudyID', 'term'])
new.to_csv('./results/zooma_mapping.csv', index=False)
