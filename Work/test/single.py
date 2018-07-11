# single
# Created by JKChang
# 11/07/2018, 16:23
# Tag:
# Description: 

from owlready2 import *

from Work.ontology_info import *

onto_path = '/Users/jkchang/Github/Python/large file/ncbitaxon.owl'
print('loading ontology ... ')
onto = get_ontology(onto_path).load()
print('finish loading... ')

f = information(onto)
print(f.get_supers('Arabidopsis thaliana'))
print(f.super_count('Arabidopsis thaliana'))
print(f.get_subs('http://purl.obolibrary.org/obo/NCBITaxon_3702'))
print(f.sub_count('http://purl.obolibrary.org/obo/NCBITaxon_3702'))