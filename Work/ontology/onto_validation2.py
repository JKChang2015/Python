# onto_validation2
# Created by JKChang
# 2019-03-25, 11:13
# Tag:
# Description: solve incorrect factors

import json

import numpy as np
import pandas as pd
from owlready2 import urllib

# 1. exact mapping
df = pd.read_csv('incorrect.tsv', sep='\t')

# 'studyID', 'Study Factor Name', 'Study Factor Type', 'Study Factor Type Term Accession Number'

onto_list = ['EFO', 'NCIT', 'CHEBI', 'CHEMO', 'OBI', 'BAO','OMIT','SIO','MICRO']


def searchOLS(term, onto_list="*"):

    res = []
    print('Seaching ' + term + ' ...')
    if type(onto_list) == list:
        onto = ','.join([x.lower() for x in onto_list])
    else:
        onto = '*'

    try:
        url = 'https://www.ebi.ac.uk/ols/api/search?q=' + term.replace(' ', "+") + \
              '&groupField=true' \
              '&ontology=' + onto + \
              '&queryFields=label' \
              '&fieldList=iri,label,ontology_name,description,ontology_prefix' \
              '&exact=true'
        # print(url)

        fp = urllib.request.urlopen(url)
        content = fp.read().decode('utf-8')
        j_content = json.loads(content)
        responses = j_content["response"]['docs']

        for term in responses:
            d = {'Study Factor Type': '', 'Study Factor Type Term Accession Number': '', 'Definition': ''}

            try:
                d['Definition'] = term['description'][0]
            except:
                pass

            try:
                d['Study Factor Type'] = term['label']
            except:
                pass

            try:
                d['Study Factor Type Term Accession Number'] = term['iri']
            except:
                pass

            res.append(d)

        return res

    except:
        pass


df_split = pd.DataFrame(
    columns=['studyID', 'Study Factor Name', 'Study Factor Type', 'Study Factor Type Term Accession Number',
             'Definition'])

df_rest = pd.DataFrame(columns=df.columns)

for index, row in df.iterrows():
    try:
        temp = row.copy()
        respo = searchOLS(temp['Study Factor Name'])
        # respo = searchOLS(temp['Study Factor Name'], onto_list)
        if len(respo) > 0:
            df_split.loc[len(df_split)] = temp
            cat = pd.DataFrame(respo)
            df_split = df_split.append(cat, sort=False)
        else:
            df_rest.loc[len(df_rest)] = temp
    except:
        pass


count = len(df_split)-(df_split['studyID'].isnull().sum())

df_split = df_split.replace(np.nan, '', regex=True)
df_rest = df_rest.replace(np.nan, '', regex=True)

df_split.to_csv('OLS mapped all onto.tsv', sep='\t', index=False)
df_rest.to_csv('OLS unmapped all onto.tsv', sep='\t', index=False)

print()

# def getOLSTerm(keyword):
#     logger.info('Requesting OLS...')
#     print('Requesting OLS...')
#     res = []
#
#     if keyword in [None, '']:
#         return res
#
#     try:
#         # https://www.ebi.ac.uk/ols/api/search?q=lung&groupField=true&queryFields=label,synonym&fieldList=iri,label,short_form,obo_id,ontology_name,ontology_prefix
#         url = 'https://www.ebi.ac.uk/ols/api/search?q=' + keyword.replace(' ', "+") + \
#               '&groupField=true' \
#               '&queryFields=label,synonym' \
#               'fieldList=iri,label,short_form,ontology_name,description,ontology_prefix' \
#               '&rows=30'  # &exact=true
#         fp = urllib.request.urlopen(url)
#         content = fp.read().decode('utf-8')
#         j_content = json.loads(content)
#         responses = j_content["response"]['docs']
#
#         for term in responses:
#             name = ' '.join(
#                 [w.title() if w.islower() else w for w in term['label'].split()])
#
#             try:
#                 definition = term['description'][0]
#             except:
#                 definition = ''
#
#             try:
#                 ontoName = term['ontology_prefix']
#                 provenance_name = term['ontology_prefix']
#             except:
#                 ontoName = ''
#                 provenance_name = ''
#
#             enti = entity(name=name, iri=term['iri'], definition=definition, ontoName=ontoName,
#                           provenance_name=provenance_name)
#
#             res.append(enti)
#             if len(res) >= 20:
#                 break
#
#     except Exception as e:
#         print(e.args)
#         logger.error('getOLS' + str(e))
#     return res
