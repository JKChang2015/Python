# t
# Created by JKChang
# 26/06/2018, 14:47
# Tag:
# Description: 

from owlready2 import *

from Work.ontology_info import *

onto = get_ontology('file:///Users/jkchang/Downloads/ncit.owl').load()
f = information(onto)
# print(f.get_supers('pink lady'))
# print(f.super_count('pink lady'))
print(f.get_subs('Investigator'))
# print(f.sub_count('http://purl.enanomapper.org/onto/ENM_9000014'))
# print(f.get_iri('pink lady'))


a = ['cat', 'dog', 'fish']
response = [{'animal':x} for x in a]
print(response)