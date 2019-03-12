# add_entity
# Created by JKChang
# 2019-03-12, 10:56
# Tag:
# Description: add new class from the spread sheet

from owlready2 import get_ontology, urllib, IRIS
import owlready2

label = 'kiwi'
definition = 'kind of green fruit'
superclass = 'fruit'

onto = get_ontology('../resources/plant.owl').load()
print(type(onto))
with onto:
    cls = onto.search_one(label=superclass)

    class MTBLS100(cls):
        pass
    print(type(MTBLS100))
    MTBLS100.label = label
    MTBLS100.isDefinedBy = definition

onto.save(file='fruit added.owl',format='rdfxml')

# print(cls.isDefinedBy)
# # print(onto.base_iri)
# # print(onto.classes())
# # pro = list(onto.properties())
# # print(pro)



print()



