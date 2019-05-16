# add
# Created by JKChang
# 2019-05-16, 11:52
# Tag:
# Description: 

from owlready2 import get_ontology
import re

onto = get_ontology('./resources/metabolights.owl').load()

temp = []
for c in onto.classes():
    if str(c).startswith('metabolights'):
        temp.append(str(c))

last = max(temp)
temp = str(int(last[-6:]) + 1).zfill(6)
id = 'MTBLS_'+temp
# temp.sort(reverse=True)
print(id)

print(max(temp))
print(max(temp)+1)
print()