# OLS
# Created by JKChang
# 20/09/2018, 12:00
# Tag:
# Description:  pares the the json response from the EBI OLS API

import json
import urllib.request
import pandas as pd


def getOLS(query):
    url = 'https://www.ebi.ac.uk/ols/api/select?q=' + query.replace(' ', "+")
    fp = urllib.request.urlopen(url)
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

fd = pd.read_csv('factors.csv')
terms = fd['terms']

for term in terms:
    temp = [term]

    match = getOLS(term)
    for i in match.keys():
        temp.append(match[i])
        temp.append(i)

    s = ','.join(temp) + '\n'
    with open('factor test.csv', 'a') as file:
        file.writelines(s)

