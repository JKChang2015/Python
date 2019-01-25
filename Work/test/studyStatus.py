# studyStatus
# Created by JKChang
# 2019-01-25, 11:45
# Tag:
# Description:

import json
import re
import urllib.request
from io import BytesIO
from zipfile import ZipFile

import pandas as pd

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


for studyID in studyIDs:
    try:
        url = 'http://ves-ebi-90.ebi.ac.uk:5000/metabolights/swagger/ws/studies/' + studyID + '/meta-info'
        request = urllib.request.Request(url)
        request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        j_content = json.loads(content)

        resp = dict(e.split(':') for e in j_content['data'])
        print(studyID, resp['status'])
    except:
        print(studyID)