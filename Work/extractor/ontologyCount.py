# ontologyCount
# Created by JKChang
# 10/09/2019, 10:54
# Tag:
# Description: statistic ontology for all studies

import json
import re

import numpy as np
import pandas as pd
from owlready2 import urllib

from Work.extractor import studyList


class factor():
    def __init__(self, studyID, name, type, iri):
        self.studyID = studyID
        self.name = name
        self.type = type
        self.iri = iri


def getOnto_Name(iri):
    # get ontology name by giving iri of entity
    try:
        url = 'http://www.ebi.ac.uk/ols/api/terms/findByIdAndIsDefiningOntology?iri=' + iri
        fp = urllib.request.urlopen(url)
        content = fp.read().decode('utf-8')
        j_content = json.loads(content)
        print(iri + '  ---->' + j_content['_embedded']['terms'][0]['ontology_prefix'])
        return j_content['_embedded']['terms'][0]['ontology_prefix']
    except:
        if 'Thesaurus.owl' in iri:
            return "NCIT"
        if 'bao#BAO' in iri:
            return 'BAO'
        if 'SNOMEDCT' in iri:
            return 'SNOMEDCT'
        if 'XEO' in iri:
            return 'XEML'
        if 'MESH' in iri:
            return 'MESH'
        if 'PATO' in iri:
            return 'PATO'
        else:
            print(iri + '  ---->   *******')
            return np.nan


studyIDs = studyList.getStudyIDs()

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'

facts = []

for studyID in studyIDs:
    filePath = folderPath + studyID + '/i_Investigation.txt'

    try:
        with open(filePath) as f:
            text = ''
            for line in f.readlines():
                if line.startswith('Study Factor Name\t') or \
                        line.startswith('Study Factor Type\t') or \
                        line.startswith('Study Factor Type Term Accession Number\t'):
                    text = text + line
            lines = text.split('\n')
            names, types, iris = [], [], []

            for line in lines:
                if line.startswith('Study Factor Name\t'):
                    names = list(re.findall(r'"([^"]*)"', line))
                if line.startswith('Study Factor Type\t'):
                    types = list(re.findall(r'"([^"]*)"', line))
                if line.startswith('Study Factor Type Term Accession Number\t'):
                    iris = list(re.findall(r'"([^"]*)"', line))

            if len(names) == len(types) == len(iris):
                for name, type, iri in zip(names, types, iris):
                    print(studyID, name, type, iri)
                    fact = factor(studyID, name, type, iri)
                    facts.append(fact)
            else:
                pass
    except:
        print("Fail to open investigation file in " + studyID)

df = pd.DataFrame(columns=['studyID', 'name', 'type', 'iri', 'ontoName'])
for fact in facts:
    try:

        temp = pd.Series([fact.studyID, fact.name, fact.type, fact.iri, ''], index=df.columns)
        df = df.append(temp, ignore_index=True)
    except:
        print('something wrong with ' + fact.studyID)

df['iri'].replace('', np.nan, inplace=True)
df = df.dropna(subset=['iri'])
df['ontoName'] = df['iri'].apply(lambda x: getOnto_Name(x))

c = df['ontoName'].value_counts(dropna=True)
df.to_csv('ontology Counts.tsv', sep='\t', index=False)
print()
