# factors
# Created by JKChang
# 2019-01-23, 15:40
# Tag:
# Description: extract factors


import json
import re
import traceback
import urllib.request
from io import BytesIO
from zipfile import ZipFile

import pandas as pd
import psycopg2

import config


class factor():
    def __init__(self, studyID, name, type, iri):
        self.studyID = studyID
        self.name = name
        self.type = type
        self.iri = iri


url = 'https://www.ebi.ac.uk/metabolights/webservice/study/list'
request = urllib.request.Request(url)
request.add_header('user_token', config.Token)
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


def get_study_status():
    query_user_access_rights = """
     select case when status = 0 then 'Submitted' when status = 1 then 'In Curation' when status = 2 then 'In Review' 
             when status = 3 then 'Public' else 'Dormant' end as status, 
        acc from studies;
    """
    token = config.Token

    def execute_query(query, user_token, study_id=None):
        try:
            params = config.DB_PARAMS
            conn = psycopg2.connect(**params)
            cursor = conn.cursor()
            query = query.replace('\\', '')
            if study_id is None:
                cursor.execute(query, [user_token])
            else:
                query2 = query_user_access_rights.replace("#user_token#", user_token)
                query2 = query2.replace("#study_id#", study_id)
                cursor.execute(query2)
            data = cursor.fetchall()
            conn.close()

            return data

        except psycopg2.Error as e:
            print("Unable to connect to the database")
            print(e.pgcode)
            print(e.pgerror)
            print(traceback.format_exc())

    study_list = execute_query(query_user_access_rights, token)
    study_status = {}
    for study in study_list:
        study_status[study[1]] = study[0]

    return study_status


status = get_study_status()
print(len(studyIDs))
studyIDs = [studyID for studyID in studyIDs if status[studyID] == 'Public' or status[studyID] == 'In Review']
print(len(studyIDs))
c = 0

for studyID in studyIDs:  # for each study
    c = c + 1

    u = 'https://www.ebi.ac.uk/metabolights/' + studyID + '/files/i_Investigation.txt?token=' + config.Token
    # u = 'https://www.ebi.ac.uk/metabolights/' + studyID + '/files/i_Investigation.txt'
    # print(u)
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
            print(c, studyID, name, type, iri)
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
