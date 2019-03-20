# getAllOnto
# Created by JKChang
# 2019-03-19, 14:10
# Tag:
# Description: 

from owlready2 import  urllib
import json
import time

start = time.time()
url = 'https://www.ebi.ac.uk/ols/api/ontologies?page=0&size=500'
fp = urllib.request.urlopen(url)
content = fp.read().decode('utf-8')
j_content = json.loads(content)

res = {}
for onto in j_content['_embedded']['ontologies']:
    ontoInfo = {}
    ontoInfo['title'] = onto['config']['title']
    ontoInfo['prefix'] = onto['config']['preferredPrefix']
    ontoInfo['version'] = onto['config']['version']
    ontoInfo['url'] = onto['config']['id']
    res[onto['config']['title']] = ontoInfo

print(time.time()-start)

for x in res:
    print (x)
    for y in res[x]:
        print (y,':',res[x][y])
    print('-'*25)
