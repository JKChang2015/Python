# investigation file
# Created by JKChang
# 2018-11-29, 14:29
# Tag:
# Description: download investigation file

import re
import urllib.request
from io import BytesIO
from zipfile import ZipFile


class entity():
    def __init__(self, studyID, term, iri):
        self.studyID = studyID
        self.term = term
        self.iri = iri


studyID = 'MTBLS372'
u = 'http://www.ebi.ac.uk/metabolights/' + studyID + '/files/i_Investigation.txt?token=15fef9e0-9187-4c8a-857d-93d8e7df53d0'
url = urllib.request.urlopen(u)
text = ''

with ZipFile(BytesIO(url.read())) as my_zip_file:
    for contained_file in my_zip_file.namelist():
        for line in my_zip_file.open(contained_file).readlines():
            if line.decode().startswith('Study Assay Technology Type'):
                text = text + line.decode()

# print(studyID + '-' * 30)
# print(text)
res =  []
lines = text.split('\n')
term, iri = '', ''


for line in lines:
    if line.startswith('Study Assay Technology Type	'):
        term = list(set(re.findall(r'"([^"]*)"', line)))
    if line.startswith('Study Assay Technology Type Term Accession Number'):
        iri = list(set(re.findall(r'"([^"]*)"', line)))

for term, iri in zip(term, iri):
    enti = entity(studyID, term, iri)
    res.append(enti)

print(res)

# url = 'https://www.ebi.ac.uk/metabolights/webservice/study/list'
# request = urllib.request.Request(url)
# request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# j_content = json.loads(content)
#
# text_final = ''
# for studyID in j_content['content']:
#     # url = 'http://www.ebi.ac.uk/metabolights/'+studyID+'/files/i_Investigation.txt?token=15fef9e0-9187-4c8a-857d-93d8e7df53d0'
#     # request = urllib.request.Request(url)
#     # request.add_header('user_token', 'b6cb38b7-8504-43bf-9281-a0c68fc06263')
#
#     u = 'http://www.ebi.ac.uk/metabolights/' + studyID + '/files/i_Investigation.txt?token=15fef9e0-9187-4c8a-857d-93d8e7df53d0'
#     url = urllib.request.urlopen(u)
#     text = ''
#
#     with ZipFile(BytesIO(url.read())) as my_zip_file:
#         for contained_file in my_zip_file.namelist():
#             # with open(("unzipped_and_read_" + contained_file + ".file"), "wb") as output:
#             for line in my_zip_file.open(contained_file).readlines():
#                 # if line.decode().startswith('Study Assay Measurement Type') o
#                       if line.decode().startswith('Study Assay Technology Type'):
#                     # if line.decode().startswith('Study Assay Measurement Type') or \
#                     #         line.decode().startswith('Study Assay Measurement Type Term Accession Number') or \
#
#                     #         line.decode().startswith('Study Assay Technology Type Term Accession Number'):
#                             text = text + line.decode()
#                             text_final = text_final + text
#
#     # left = 'STUDY ASSAYS'
#     # right = 'STUDY PROTOCOLS'
#     #
#     # print(text[text.index(left) + len(left):text.index(right)])
#     print(text)
#     print(studyID + '-' * 30)
#
# print(text_final)
