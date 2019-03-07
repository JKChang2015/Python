# zooma
# Created by JKChang
# 12/09/2018, 11:24
# Tag:
# Description: zooma requests

# @import: query terms
# @import: dictionary {term:confidence}

import urllib.request
import json
import os
import pandas as pd
import re



def getZoomaTerm(keyword):
    res = {}
    url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue=' + keyword.replace(' ', "+")
    fp = urllib.request.urlopen(url)
    content = fp.read()
    json_str = json.loads(content)
    for term in json_str:
        termName = term["annotatedProperty"]['propertyValue']
        termConfidence = term['confidence']
        termURL = term['semanticTags']
        res[termName] = termConfidence
    return res


keyword = "results"
res = getZoomaTerm(keyword)
for keys,values in res.items():
    print(keys,':',values)