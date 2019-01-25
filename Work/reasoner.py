# reseaoner
# Created by JKChang
# 2019-01-23, 10:42
# Tag:
# Description: test owlready2 reasoner

from owlready2 import *
import os

onto = get_ontology("file://./resources/pizza.owl").load()
print(onto.base_iri)


