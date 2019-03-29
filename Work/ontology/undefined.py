# undefined
# Created by JKChang
# 2019-03-29, 10:16
# Tag:
# Description: extract all undefined entities from ontology


import pandas as pd
from owlready2 import urllib
import json

from owlready2 import IRIS
from owlready2 import get_ontology


# onto = get_ontology('../resources/Metabolights.owl').load()
# undefined_term = []
# for cls in onto.classes():
#     if cls.isDefinedBy:
#         pass
#     else:
#         undefined_term.append(cls.label[0])
#
# print('\n'.join(undefined_term))

# =====
# def getOLSdefinition(term):
#     print(term)
#     try:
#         # https://www.ebi.ac.uk/ols/api/search?q=lung&groupField=true&queryFields=label,synonym&fieldList=iri,label,short_form,obo_id,ontology_name,ontology_prefix
#         url = 'https://www.ebi.ac.uk/ols/api/search?q=' + term.replace(' ', "+") + \
#               '&groupField=true' \
#               '&queryFields=label' \
#               '&type=class' \
#               '&fieldList=iri,label,description,ontology_prefix' \
#               '&rows=30'  \
#               '&exact=true'
#
#         fp = urllib.request.urlopen(url)
#         content = fp.read().decode('utf-8')
#         j_content = json.loads(content)
#         responses = j_content["response"]['docs']
#
#         for term in responses:
#             return term['description'][0]
#     except:
#         return ''
#
# df = pd.read_csv('../resources/undefined.csv')
# df['Definition'] = df['Entity name'].apply(getOLSdefinition)
# # df['Definition']= df['Definition'].replace(None,'')
# df.to_csv('../resources/undefined.tsv',index= False, sep='\t')

# =======

df = pd.read_csv('../resources/undefined.tsv', sep='\t')
df.dropna(subset=['Definition'],inplace=True)
df = df.reset_index(drop=True)

print(len(df))

onto = get_ontology('../resources/Metabolights.owl').load()


for index, row in df.iterrows():
    term = row['Entity name']
    definition = row['Definition']
    print(term)

    cls = onto.search_one(label=term)
    cls.isDefinedBy = definition

onto.save(file = "def Metabolights.owl", format = "rdfxml")


