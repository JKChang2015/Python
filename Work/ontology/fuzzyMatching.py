# fuzzyMatching
# Created by JKChang
# 2019-07-10, 09:57
# Tag:
# Description: ontology fuzzy matching


from owlready2 import *

onto = get_ontology('file://./resources/Metabolights.owl').load()

labels = []

query = 'Lipid'

for cls in onto.classes():
    labels.append(cls.label[0])

print(labels)

l = sorted(set(labels))

duplicated = []

for i in range(len(l)):
    if (labels.count(l[i]) > 1):
        duplicated.append(l[i])

print(duplicated)

# print(labels)
# print('--'*20)
#
# res = process.extract(query,labels,scorer=fuzz.token_sort_ratio)
# print(res)
