# factors
# Created by JKChang
# 2019-01-23, 15:40
# Tag:
# Description: extract factors


import json
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


url = 'https://www.ebi.ac.uk/metabolights/webservice/study/list'
request = urllib.request.Request(url)
request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
j_content = json.loads(content)


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


studyIDs = j_content['content']
studyIDs.sort(key=natural_keys)

res = []

print(len(studyIDs))
c = 0
for studyID in studyIDs:  # for each study
    print(studyID)
    c = c + 1

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

    if len(names) == len(types) == len(iris):
        for name, type, iri in zip(names, types, iris):
            # print(c, studyID, name, type, iri)
            fact = factor(studyID, name, type, iri)
            res.append(fact)
    else:
        print('insufficient information of' + studyID)

df = pd.DataFrame(columns=['studyID', 'name', 'type', 'iri'])
for fact in res:
    try:
        temp = pd.Series([fact.studyID, fact.name, fact.type, fact.iri], index=df.columns)
        df = df.append(temp, ignore_index=True)
    except:
        print('something wrong with' + fact.studyID)

df.to_csv('factors.tsv', sep='\t', index=False)
