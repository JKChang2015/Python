# onto_statistic
# Created by JKChang
# 2019-03-25, 15:52
# Tag:
# Description: 

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

terms = set([x.lower() for x in  df['Study Factor Name'].tolist()])

onto_set = {}

# 'studyID', 'Study Factor Name', 'Study Factor Type', 'Study Factor Type Term Accession Number'

onto_list = ['EFO', 'NCIT', 'CHEBI', 'CHEMO', 'OBI', 'BAO','OMIT','SIO','MICRO']


def searchOLS(term, onto_list="*"):

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
            if term['ontology_name'] in onto_set:
                onto_set[term['ontology_name']] +=1
            else:
                onto_set[term['ontology_name']] = 1

    except:
        pass


for term in terms:
    searchOLS(term,onto_list)

print(onto_set)
ontos = pd.DataFrame.from_dict(onto_set, orient = 'index')
ontos = ontos.sort_values(by=0,ascending=False)
ontos.to_csv('onto statistics.tsv', sep='\t')


print()
