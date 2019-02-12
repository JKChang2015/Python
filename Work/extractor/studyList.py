# studyList
# Created by JKChang
# 2019-02-12, 09:07
# Tag:
# Description: get list of studies

import json
import re
import traceback
import urllib.request

import psycopg2

import config


def getStudyIDs(publicStudy=False):
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

    if publicStudy:
        studyStatus = getStudyStatus()
        studyIDs = [studyID for studyID in studyIDs if
                    studyStatus[studyID] == 'Public' or studyStatus[studyID] == 'In Review']

    return studyIDs


def getStudyStatus():
    query_user_access_rights = """
             select case 
             when status = 0 then 'Submitted' 
             when status = 1 then 'In Curation' 
             when status = 2 then 'In Review' 
             when status = 3 then 'Public' 
             else 'Dormant' end as status, 
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

# studyIDs = getStudyIDs()
# print(len(studyIDs))
# studyIDs = getStudyIDs(publicStudy=True)
# print(len(studyIDs))
