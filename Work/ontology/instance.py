# instance
# Created by JKChang
# 2019-04-10, 11:57
# Tag:
# Description: add instance of Ontology

from owlready2 import get_ontology, urllib, IRIS

onto = get_ontology('./fruit added.owl').load()
for cls in onto.classes():
    print(cls)
