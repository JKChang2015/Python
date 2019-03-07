# onto_tester
# Created by JKChang
# 2019-03-07, 13:13
# Tag:
# Description: 

from owlready2 import get_ontology, urllib, IRIS

def list_subs(onto_c, sub):
    if onto_c.label and onto_c.label == '' and onto_c.iri != 'http://www.w3.org/2002/07/owl#Thing':
        return
    for children in onto_c.subclasses():
        try:
            list_subs(children, sub)
            if len(sub)>=3:
                return
            sub.append(children)
        except:
            continue


onto = get_ontology('./resources/plant.owl').load()
cls = onto.search_one(label='plant')
sub = []
list_subs(cls,sub)
print()