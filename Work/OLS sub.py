# OLS sub
# Created by JKChang
# 2018-11-28, 13:13
# Tag:
# Description: get subclass of certain class

import json
import urllib.parse

from owlready2 import urllib

from Work.ontology_info import entity






def OLSbranchSearch(query, branchName, ontoName):
    def getStartIRI(start, ontoName):
        url = 'https://www.ebi.ac.uk/ols/api/search?q=' + start + '&ontology=' + ontoName  # + '&exact=true&queryFields=label'
        fp = urllib.request.urlopen(url)
        content = fp.read().decode('utf-8')
        json_str = json.loads(content)
        # print(json_str['response']['docs'])
        res = json_str['response']['docs'][0]['iri']
        # return res
        return urllib.parse.quote_plus(res)
    res = []
    branchIRI = getStartIRI(branchName, ontoName)
    query = query.replace(' ', '%20')
    url = 'https://www.ebi.ac.uk/ols/api/search?q=' + query + '&rows=20&ontology=' + ontoName + '&allChildrenOf=' + branchIRI
    fp = urllib.request.urlopen(url)
    content = fp.read().decode('utf-8')
    json_str = json.loads(content)

    for ele in json_str['response']['docs']:
        enti = entity(name=ele['label'],
                      iri=ele['iri'],
                      obo_ID=ele['short_form'],
                      ontoName=ele['ontology_prefix'])
        res.append(enti)
    return res


p = OLSbranchSearch("instrument", "instrument", "msio")
print(p)

# /ols/api/search?q={query}&queryFields={label,synonym}
# url = 'https://www.ebi.ac.uk/ols/api/ontologies/msio/terms/'

#     https://www.ebi.ac.uk/ols/api/ontologies/msio/terms/http%253A%252F%252FnmrML.org%252FnmrCV%2523NMR%253A1000463
