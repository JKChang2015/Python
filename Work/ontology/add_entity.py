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

onto = get_ontology('./resources/metabolights.owl').load()
# onto = get_ontology('../resources/Metabolights.owl').load()

namespace = onto.get_namespace('http://www.ebi.ac.uk/metabolights/ontology/')
with namespace:
    cls = onto.search_one(label='role')
    class MTBLS1001(cls):
        pass
    print(type(MTBLS1001))
    MTBLS1001.label = 'papaya'
    MTBLS1001.isDefinedBy = 'papaya def'


for c in onto.classes():
    print(c)

# with onto:
#     cls = onto.search_one(label = 'apple')
#     d = cls.isDefinedBy
#     print(d)
#
#
# with onto:
#     cls = onto.search_one(label=superclass)
#
#     class MTBLS100(cls):
#         pass
#     print(type(MTBLS100))
#     MTBLS100.label = label
#     MTBLS100.isDefinedBy = definition


onto.save(file='fruit added.owl',format='rdfxml')

# print(cls.isDefinedBy)
# # print(onto.base_iri)
# # print(onto.classes())
# # pro = list(onto.properties())
# # print(pro)



print()



