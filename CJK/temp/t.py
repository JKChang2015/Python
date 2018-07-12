# t
# Created by JKChang
# 12/07/2018, 11:43
# Tag:
# Description: 

import json

temp = '''    {
        "comments": [],
        "annotationValue": "investigator",
        "termSource": {
            "comments": [],
            "name": "EFO",
            "file": "http://data.bioontology.org/ontologies/EFO",
            "version": "132",
            "description": "Experimental Factor Ontology"
        },
        "termAccession": "http://www.ebi.ac.uk/efo/EFO_0001739"
    }'''

d = json.loads(temp)
d['annotationValue'] = 'curator'
print(d)

