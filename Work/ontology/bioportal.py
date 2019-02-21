# bioportal
# Created by JKChang
# 28/09/2018, 09:36
# Tag:
# Description: pares the the json response from the Bioportal API

import json
import urllib.request
import pandas as pd

def getOLS(query):
    url = 'http://data.bioontology.org/search?q=' + query.replace(' ', "+") +'&require_exact_match=true'
    headers = {'Authorization': 'apikey token=c60c5add-63c6-4485-8736-3f495146aee3'}

    request = urllib.request.Request(url)
    request.add_header(headers)
    fp = request.get(url,headers=headers)
    # fp = urllib.request.urlopen(url)
    content = fp.read()
    j_content = json.loads(content)
    responses = j_content["response"]['docs'][:5]
    res = {}
    for term in responses:
        label = term['label']
        iri = term['iri']
        if iri not in res.keys():
            res[iri] = label
    print(res)
    return res

getOLS('homo sapiens')