# placeholder
# Created by JKChang
# 2019-07-18, 10:50
# Tag:
# Description: extract placeholder from study investigation file

import re

import pandas as pd

from Work.extractor import studyList


class factor():
    def __init__(self, studyID, name, type, iri):
        self.studyID = studyID
        self.name = name
        self.type = type
        self.iri = iri


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
            names, types, iris = [], [], []

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

                if line.startswith('Study Design Type Term Source REF\t'):
                    if line.__contains__('"'):
                        types = list(re.findall(r'"([^"]*)"', line))
                    else:
                        types = line.split('\t')[1:]

            if len(names) == len(types) == len(iris):
                for name, type, iri in zip(names, types, iris):
                    if iri == 'http://www.ebi.ac.uk/metabolights/ontology/placeholder':
                        print(studyID, name, type, iri)
                        # fact = {studyID, name, type, iri}
                        fact = factor(studyID, name, type, iri)
                        res.append(fact)
            else:
                print('insufficient information of' + studyID)
    except:
        # print('can not open investigation file from ' + studyID)
        pass

df = pd.DataFrame(columns=['StudyID', 'name', 'type', 'iri'])

for r in res:
    temp = pd.Series([r.studyID, r.name, r.type, r.iri], index=df.columns)
    df = df.append(temp, ignore_index=True)

df.to_csv('placeHolder.tsv', sep='\t', index=False)

print()
