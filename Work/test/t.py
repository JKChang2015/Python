# t
# Created by JKChang
# 26/06/2018, 14:47
# Tag:
# Description: 

from owlready2 import *
from Work.ontology.onto_info import *

onto = get_ontology('../resources/Metabolights.owl').load()
info = information(onto)

cls = onto.search_one(label = 'age')
subs = info.get_subs(cls)

for x in subs:
    print(x.label)

query = 'age'




def find_factor(cluster, query):
    for cls in cluster:
         if query == cls.label:
             return cls
         try:
             factors = info.get_factors(cls)
             if query in factors:
                 return cls
         except:
             pass
    print('No factors for %s' %query)
    return None


res = find_factor(subs,query)
print(res.label)




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


