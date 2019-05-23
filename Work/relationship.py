# relationship
# Created by JKChang
# 17/07/2018, 15:08
# Tag:
# Description: extract relationships from class

from owlready2 import *

onto = get_ontology('file://./resources/Metabolights.owl').load()

typo = IRIS['http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym']
exact = IRIS['http://www.geneontology.org/formats/oboInOwl#hasExactSynonym']
c = onto.search_one(label="Homo sapiens")

print(type(c))

print(typo[c])
print(exact[c])
