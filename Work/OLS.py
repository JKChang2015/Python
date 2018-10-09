# OLS
# Created by JKChang
# 20/09/2018, 12:00
# Tag:
# Description:  pares the the json response from the EBI OLS API

import json
import ssl
import urllib.request

from Work.ontology_info import entity


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


# fd = pd.read_csv('factors.csv')
# terms = fd['terms']
#
# for term in terms:
#     temp = [term]
#
#     match = getOLS(term)
#     for i in match.keys():
#         temp.append(match[i])
#         temp.append(i)
#
#     s = ','.join(temp) + '\n'
#     with open('factor test.csv', 'a') as file:
#         file.writelines(s)


def getOLSTerm(keyword):
    res = []
    try:
        url = 'https://www.ebi.ac.uk/ols/api/search?q=' + keyword.replace(' ', "+") + \
              '&exact=true' \
              '&groupField=true' \
              '&queryFields=label,synonym' \
              '&fieldList=iri,label,short_form,obo_id,ontology_name,ontology_prefix'
        fp = urllib.request.urlopen(url)
        content = fp.read()
        j_content = json.loads(content)
        responses = j_content["response"]['docs']

        for term in responses:
            enti = entity(name=term['label'].title(), iri=term['iri'],
                          obo_ID=term['obo_id'], ontoName=term['ontology_prefix'])
            res.append(enti)
            if len(res) >= 5:
                break

    except Exception as e:
        pass
    return res


def getOnto_Name(iri):
    # get ontology name by giving iri of entity
    substring = iri.rsplit('/', 1)[-1]
    name = ''.join(x for x in substring if x.isalpha())
    return name


def getZoomaTerm(keyword):
    res = []
    try:
        url = 'https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue=' + keyword.replace(' ', "+")
        ssl._create_default_https_context = ssl._create_unverified_context
        fp = urllib.request.urlopen(url)
        content = fp.read().decode('utf8')
        json_str = json.loads(content)
        for term in json_str:
            iri = term['semanticTags'][0]

            enti = entity(name=term["annotatedProperty"]['propertyValue'].title(),
                          iri=iri,
                          obo_ID=iri.rsplit('/', 1)[-1],
                          ontoName=getOnto_Name(iri),
                          Zooma_confidence=term['confidence'])
            res.append(enti)
    except Exception as e:
        pass
    return res


def getBioportalTerm(keyword):
    res = []
    try:
        url = 'http://data.bioontology.org/search?q=' + keyword.replace(' ', "+") + '&require_exact_match=true'
        request = urllib.request.Request(url)
        request.add_header('Authorization', 'apikey token=c60c5add-63c6-4485-8736-3f495146aee3')
        response = urllib.request.urlopen(request)
        content = response.read()
        j_content = json.loads(content)

        iri_record = []

        for term in j_content['collection']:
            iri = term['@id']
            if iri in iri_record:
                continue

            if 'MESH' or 'mesh' in iri:
                ontoName = 'MESH'
            elif 'ncicb' in iri:
                ontoName = 'NCIT'
            else:
                ontoName = getOnto_Name(iri)

            enti = entity(name=term['prefLabel'],
                          iri=iri,
                          obo_ID=iri.rsplit('/', 1)[-1],
                          ontoName=ontoName)
            res.append(enti)
            iri_record.append(iri)
            if len(res) >= 5:
                break
    except Exception as e:
        pass
    return res


keyword = 'water'
res = getBioportalTerm(keyword)
print(res)

iri = 'http://purl.obolibrary.org/obo/UBERON_0002048'
getOnto_Name(iri)
