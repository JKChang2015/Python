# _100times
# Created by JKChang
# 2019-08-01, 16:18
# Tag:
# Description:  request py-ws 100 times get results

import json
import urllib.request
import time

keyword = 'sugar'
res = []

url = 'https://wwwdev.ebi.ac.uk/metabolights/ws/ebi-internal/ontology?branch=factor&term=' + keyword.replace(' ', '%20')

fp = urllib.request.urlopen(url)
content = fp.read().decode('utf-8')
j_content = json.loads(content)

a = 0

while a < 100:
    for i in j_content['OntologyTerm']:
        result = i['annotationValue'] + ' ' + i['termAccession']
        res.append(result)

    print(res)
    print()
    a += 1
    time.sleep(5)
