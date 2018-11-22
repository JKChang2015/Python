# mapStudy
# Created by JKChang
# 14/11/2018, 09:34
# Tag:
# Description: map terms with studies

import json
import numpy as np
import pandas as pd
from owlready2 import urllib

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


def searchStudies(query, feature='factors'):
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

    res = []
    for studyID in j_content['content']:
        print('searching', studyID)
        info = getStudyInfo(studyID)
        if feature.casefold() == 'factors'.casefold():
            fea = info.getFactors()
        elif feature.casefold() == 'organism'.casefold():
            fea = info.getOrganismName()
        elif feature.casefold() == 'organismPart'.casefold():
            fea = info.getOrganismPart()
        # elif feature == ''
        else:
            fea = None

        if fea != None and query.casefold() in (f.casefold() for f in fea):
            print('adding', studyID)
            res.append(studyID)

    res.sort(key=natural_keys)
    return res


#
# print(searchStudies('time', 'factors'))


def main():
    file_name = '/Users/jkchang/metabolights_zooma.tsv'
    table_df = pd.read_csv(file_name, sep="\t", encoding='utf-8')
    table_df = table_df.replace(np.nan, '', regex=True)

    for i in range(len(table_df)):
        query = table_df.iloc[i]['PROPERTY_VALUE']
        attribute_name = 'factor'
        res = ','.join(searchStudies(query))
        table_df.iloc[i]['STUDY'] = res
        table_df.to_csv(file_name, sep='\t', index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
