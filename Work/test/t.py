# t
# Created by JKChang
# 26/06/2018, 14:47
# Tag:
# Description: 

from owlready2 import *


from Work.onto_info import *

onto = get_ontology('../resources/Metabolights.owl').load()
info = information(onto)
# root = 'factors'
# start_cls = onto.search_one(root)

cls = onto.search_one(label='age')
sups = info.get_subs(cls)
res = [x.label[0] for x in sups]
print(res)



#
# info = information(onto)
# try:
#     cls = onto.search_one(label='age')
#     print(info.get_subs(cls))
#     print(info.get_supers(cls))
#     print(info.sub_count(cls))
#     print(info.sup_count(cls))
#     print(info.get_iri(cls))
#     print(info.get_factors(cls))
# except:
#     print("cant find it...")



# for ann_prop in onto.annotation_properties():
#     print(ann_prop)
#
# annotation = IRIS['http://www.ebi.ac.uk/metabolights/ontology/MTBLS_100000']



# apple.comment = ["A first comment on the Drug class", "A second comment"]
# onto.save(file="abbc.owl", format="rdfxml")



# http://www.ebi.ac.uk/metabolights/ontology/MTBLS_100000

# f = information(onto)
# print(f.get_supers('pink lady'))
# print(f.super_count('pink lady'))
# print(f.get_subs('Investigator'))
# print(f.sub_count('http://purl.enanomapper.org/onto/ENM_9000014'))
# print(f.get_iri('pink lady'))


