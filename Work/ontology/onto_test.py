# onto_test
# Created by JKChang
# 2019-02-25, 20:49
# Tag:
# Description:

from owlready2 import IRIS
from owlready2 import get_ontology



onto = get_ontology('../resources/Metabolights.owl').load()

# c = list(onto.classes())
c = onto.search_one(label = 'Investigator')
d = c.isDefinedBy[0]
print()