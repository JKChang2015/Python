# definition
# Created by JKChang
# 2019-02-22, 22:08
# Tag:
# Description: get definition of the class

import json
from urllib.parse import quote_plus

from owlready2 import urllib


def get_def(ontoName, iri):
    try:
        ir = quote_plus(quote_plus(iri))
        url = 'https://www.ebi.ac.uk/ols/api/ontologies/' + ontoName + '/terms/' + ir
        fp = urllib.request.urlopen(url)
        content = fp.read().decode('utf-8')
        json_str = json.loads(content)
        return json_str['description'][0]
    except:
        return ''


print(get_def('NCIT', 'http://purl.obolibrary.org/obo/NCIT_C34808'))
