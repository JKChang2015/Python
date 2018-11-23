# studyInfo
# Created by JKChang
# 2018-11-22, 13:51
# Tag:
# Description: extract study information from web service

import json
import re

import pandas as pd
from owlready2 import urllib


# from tqdm import tqdm


class getStudyInfo():

    def __init__(self, studyID):
        try:
            url = 'https://www.ebi.ac.uk/metabolights/webservice/study/' + studyID
            request = urllib.request.Request(url)
            request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            self.study_content = json.loads(content)
        except:
            print('cant find study', studyID)

    def getFactors(self):
        try:
            res = []
            for ele in self.study_content['content']['factors']:
                res.append(ele['name'])
            return res
        except:
            return None

    def getOrganismName(self):
        try:
            res = []
            for ele in self.study_content['content']['organism']:
                res.append(ele['organismName'])
            return res
        except:
            return None

    def getOrganismPart(self):
        try:
            res = []
            for ele in self.study_content['content']['organism']:
                res.append(ele['organismPart'])
            return res
        except:
            return None

    def getOrganismPair(self):
        try:
            return self.study_content['content']['organism']
        except:
            return None


url = 'https://www.ebi.ac.uk/metabolights/webservice/study/list'
request = urllib.request.Request(url)
request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
j_content = json.loads(content)

attribute = 'organismPart'
terms = []


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


df = pd.DataFrame(columns=['studyID', attribute])
studyIDs = j_content['content']
studyIDs.sort(key=natural_keys)

for studyID in studyIDs:
    print('extracting', studyID)
    info = getStudyInfo(studyID)

    if attribute == 'factor':
        terms = info.getFactors()
    elif attribute == 'organism':
        terms = info.getOrganismName()
    elif attribute == 'organismPart':
        terms = info.getOrganismPart()
    else:
        print('please provide attribute name')

    try:
        for term in terms:
            df = df.append(pd.Series([studyID, term], index=df.columns), ignore_index=True)
    except:
        print('No terms in', studyID)

df.to_csv('/Users/jkchang/study organismPart.tsv', index=False, sep='\t', encoding='utf-8')

