# onto_test
# Created by JKChang
# 2019-02-25, 20:49
# Tag:
# Description:

from owlready2 import IRIS
from owlready2 import get_ontology

from Work.ontology.ontology_info import entity
from Work.ontology.ontology_info import onto_information



onto = get_ontology('../resources/Metabolights.owl').load()
c = list(onto.classes())
# start_cls = onto.search_one(iri='http://www.w3.org/2002/07/owl#Thing')
start_cls = onto.search_one(label='factors')
res = onto.search(is_a = start_cls)
print()