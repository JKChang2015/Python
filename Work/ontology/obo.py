# obo
# Created by JKChang
# 2019-04-29, 10:54
# Tag:
# Description: method to extract classes information from obo file

import pronto

onto = pronto.Ontology('./resources/chebi_lite.obo')
parents = onto['CHEBI:24867'].rparents()
print(parents.name)


