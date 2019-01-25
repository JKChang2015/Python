# factor_test
# Created by JKChang
# 2019-01-25, 09:59
# Tag:
# Description: test factor space

import re
import urllib.request
from io import BytesIO
from zipfile import ZipFile

import pandas as pd


class factor():
    def __init__(self, studyID, name, type, iri):
        self.studyID = studyID
        self.name = name
        self.type = type
        self.iri = iri


res = []
studyID = 'MTBLS9'

u = 'http://www.ebi.ac.uk/metabolights/' + studyID + '/files/i_Investigation.txt?token=15fef9e0-9187-4c8a-857d-93d8e7df53d0'
url = urllib.request.urlopen(u)
text = ''

with ZipFile(BytesIO(url.read())) as my_zip_file:
    for contained_file in my_zip_file.namelist():

        for line in my_zip_file.open(contained_file).readlines():
            if line.decode().startswith('Study Factor Name\t') or \
                    line.decode().startswith('Study Factor Type\t') or \
                    line.decode().startswith('Study Factor Type Term Accession Number\t'):
                text = text + line.decode()

lines = text.split('\n')
names, types, iris = [], [], []

for line in lines:
    if line.startswith('Study Factor Name\t'):
        names = list(re.findall(r'"([^"]*)"', line))
    if line.startswith('Study Factor Type\t'):
        types = list(re.findall(r'"([^"]*)"', line))
    if line.startswith('Study Factor Type Term Accession Number\t'):
        iris = list(re.findall(r'"([^"]*)"', line))

for name, type, iri in zip(names, types, iris):
    print(studyID, name, type, iri)
    fact = factor(studyID, name, type, iri)
    res.append(fact)

df = pd.DataFrame(columns=['studyID', 'name', 'type', 'iri'])
for fact in res:
    try:
        temp = pd.Series([fact.studyID, fact.name, fact.type, fact.iri], index=df.columns)
        df = df.append(temp, ignore_index=True)
    except:
        print('something wrong with' + studyID)

df.to_csv('factors.tsv', sep='\t', index=False)