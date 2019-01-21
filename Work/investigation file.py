# investigation file
# Created by JKChang
# 2018-11-29, 14:29
# Tag:
# Description: download investigation file

import json
import numpy as np
import pandas as pd
import re

import urllib.request
from io import BytesIO
from zipfile import ZipFile


class entity():
    def __init__(self, studyID, term, iri):
        self.studyID = studyID
        self.term = term
        self.iri = iri


url = 'https://www.ebi.ac.uk/metabolights/webservice/study/list'
request = urllib.request.Request(url)
request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
j_content = json.loads(content)

import re


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
    c = c + 1


    u = 'http://www.ebi.ac.uk/metabolights/' + studyID + '/files/i_Investigation.txt?token=15fef9e0-9187-4c8a-857d-93d8e7df53d0'
    url = urllib.request.urlopen(u)
    text = ''

    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():

            for line in my_zip_file.open(contained_file).readlines():
                      if line.decode().startswith('Study Assay Technology Type'):
                            text = text + line.decode()

    lines = text.split('\n')
    terms,iris = [],[]

    for line in lines:
        if line.startswith('Study Assay Technology Type	'):
            terms = list(set(re.findall(r'"([^"]*)"', line)))
        if line.startswith('Study Assay Technology Type Term Accession Number'):
            iris = list(set(re.findall(r'"([^"]*)"', line)))

    for term, iri in zip(terms, iris):
        print(c,studyID,term,iri)
        enti = entity(studyID, term, iri)
        res.append(enti)

df = pd.DataFrame(columns=['studyID','term','iri'])
for enti in res:
    temp = pd.Series([enti.studyID,enti.term,enti.iri],index=df.columns)
    df = df.append(temp,ignore_index=True)

df.to_csv('investigation.tsv',sep='\t',index=False)