# obo
# Created by JKChang
# 2019-04-29, 10:54
# Tag:
# Description: method to extract classes information from obo file

import pronto

onto = pronto.Ontology('../resources/psi-ms.obo')

cl = onto['CHEBI:24867']
print(cl.name)


