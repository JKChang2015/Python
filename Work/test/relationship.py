# relationship
# Created by JKChang
# 17/07/2018, 15:08
# Tag:
# Description: extract relationships from class

from owlready2 import *

onto = get_ontology('file://demo.owl').load()
cl = onto.get_namespace(onto.base_iri)
cl.ontology.name