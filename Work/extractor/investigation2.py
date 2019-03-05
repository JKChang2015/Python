# investigation2
# Created by JKChang
# 2019-02-11, 09:37
# Tag:
# Description: extract certain content from the investigation file


import json
import re
import traceback
import urllib.request

import pandas as pd
import paramiko
import psycopg2

import config


def getStudyIDs():
    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        return [atoi(c) for c in re.split('(\d+)', text)]

    url = 'https://www.ebi.ac.uk/metabolights/webservice/study/list'
    request = urllib.request.Request(url)
    request.add_header('user_token', config.Token)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    j_content = json.loads(content)

    studyIDs = j_content['content']
    studyIDs.sort(key=natural_keys)

    return studyIDs


def getStudyStatus():
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


class factor():
    def __init__(self, studyID, name, type, iri):
        self.studyID = studyID
        self.name = name
        self.type = type
        self.iri = iri


def getFactors(studyID):
    res = []
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(config.SSH_PARAMS['host'], username=config.SSH_PARAMS['user'],
                   password=config.SSH_PARAMS['password'])
    sftp_client = client.open_sftp()
    address = '/net/isilonP/public/rw/homes/tc_cm01/metabolights/prod/studies/stage/private/' + studyID + \
              '/i_Investigation.txt'
    with sftp_client.open(address) as f:
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
                res.append(fact)
        else:
            print('insufficient information of' + studyID)

    return res


class design():
    def __init__(self, studyID, type, iri):
        self.studyID = studyID
        self.type = type
        self.iri = iri


def getStudyDesign(studyID):
    res = []
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(config.SSH_PARAMS['host'], username=config.SSH_PARAMS['user'],
                   password=config.SSH_PARAMS['password'])
    sftp_client = client.open_sftp()
    address = '/net/isilonP/public/rw/homes/tc_cm01/metabolights/prod/studies/stage/private/' + studyID + \
              '/i_Investigation.txt'
    try:
        with sftp_client.open(address) as f:
            text = ''
            for line in f.readlines():
                if line.startswith('Study Design Type\t') or \
                        line.startswith('Study Design Type Term Accession Number'):
                    text = text + line
            lines = text.split('\n')
            studyTypes, iris = [], []

            for line in lines:
                if line.startswith('Study Design Type\t'):
                    studyTypes = list(re.findall(r'"([^"]*)"', line))
                if line.startswith('Study Design Type Term Accession Number\t'):
                    iris = list(re.findall(r'"([^"]*)"', line))

            if len(studyTypes) == len(iris) == len(iris):
                for studyType, iri in zip(studyTypes, iris):
                    print(studyID, studyType, iri)
                    studydesign = design(studyID, studyType, iri)
                    res.append(studydesign)
            else:
                print('insufficient information of' + studyID)
    except:
        print('fail to connect ', studyID)

    return res


res = []
studyIDs = getStudyIDs()
studyStatus = getStudyStatus()
studyIDs = [studyID for studyID in studyIDs if studyStatus[studyID] == 'Public' or studyStatus[studyID] == 'In Review']

for studyID in studyIDs:
    # print(studyID)
    temp = getStudyDesign(studyID)
    res = res + temp

df = pd.DataFrame(columns=['studyID', 'type', 'iri'])
for target in res:
    try:
        temp = pd.Series([target.studyID, target.type, target.iri], index=df.columns)
        df = df.append(temp, ignore_index=True)
    except:
        print('something wrong with' + target.studyID)

df.to_csv('target.tsv', sep='\t', index=False)
