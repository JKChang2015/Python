# branch_searching
# Created by JKChang
# 15/11/2019, 10:27
# Tag:
# Description: search terms in the particular branch

from owlready2 import *

onto = get_ontology('file://./resources/plant.owl').load()

keyword = 'apple'
branch = 'flower'

branch_term = onto.search_one(label=branch)

subs = branch_term.descendants()
for i in subs:
    print(i.label)

cls = onto.search(label=keyword, _case_sensitive=False)

subs.remove(branch_term)

for i in cls:
    print(i.label)

h = list(subs).remove(onto.search_one(label=branch))

res = list(set(subs) & set(cls))

for i in res:
    print(i.label)

print()

sup = onto.search_one(label='fruit')

subs = sup.descendants()

print(subs)

for i in subs:
    print(i.label)

res = onto.search(descendants=sup, label='apple')

for i in res:
    print(i.label)

print()
