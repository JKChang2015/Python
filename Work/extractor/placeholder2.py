# placeholder2
# Created by JKChang
# 2019-08-20, 10:55
# Tag:
# Description: 

import json
import re

import pandas as pd
from owlready2 import urllib

from Work.extractor import studyList


def matchOnto(term):
    url = 'http://localhost:5005/metabolights/ws/ebi-internal/ontology?term=' + term.replace(' ', "+")
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    j_content = json.loads(content)

    for res in j_content['OntologyTerm']:
        if res['annotationValue'].lower() == term.lower():
            return res['annotationValue'], res['termSource']['name'], res['termAccession']

        if res['annotationValue'].lower().startswith(term.lower()):
            return "*" + res['annotationValue'], res['termSource']['name'], res['termAccession']

    return ' ', ' ', ' '


class factor():
    def __init__(self, studyID, name, matchname, matchtype, matchiri):
        self.studyID = studyID
        self.name = name
        self.matchname = matchname
        self.matchtype = matchtype
        self.matchiri = matchiri


studyIDs = studyList.getStudyIDs()
# studyIDs = ['MTBLS930']
res = []

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'

for studyID in studyIDs:
    filePath = folderPath + studyID + '/i_Investigation.txt'
    try:
        # print(studyID)
        with open(filePath) as f:
            text = ''
            for line in f.readlines():
                if line.startswith('Study Design Type\t') or \
                        line.startswith('Study Design Type Term Accession Number\t') or \
                        line.startswith('Study Design Type Term Source REF\t'):
                    text = text + line
            lines = text.split('\n')
            names, iris = [], []

            for line in lines:
                if line.startswith('Study Design Type\t'):
                    if line.__contains__('"'):
                        names = list(re.findall(r'"([^"]*)"', line))
                    else:
                        names = line.split('\t')[1:]

                if line.startswith('Study Design Type Term Accession Number\t'):
                    if line.__contains__('"'):
                        iris = list(re.findall(r'"([^"]*)"', line))
                    else:
                        iris = line.split('\t')[1:]

            if len(names) == len(iris):
                for name, iri in zip(names, iris):
                    if iri == 'http://www.ebi.ac.uk/metabolights/ontology/placeholder':
                        matchname, matchtype, matchiri = matchOnto(name)

                        print(studyID, name, matchname, matchtype, matchiri)

                        fact = factor(studyID, name, matchname, matchtype, matchiri)
                        res.append(fact)
            else:
                print('insufficient information of' + studyID)
    except:
        pass

df = pd.DataFrame(columns=['StudyID', 'name', 'matched to', 'matched type', 'matched iri'])

for r in res:
    temp = pd.Series([r.studyID, r.name, r.matchname, r.matchtype, r.matchiri], index=df.columns)
    df = df.append(temp, ignore_index=True)
    df = df.sort_values(by=['matched to', 'matched type', 'matched iri'], ascending=False)
#
df.to_csv('placeHolder 2.tsv', sep='\t', index=False)
#
# print()
