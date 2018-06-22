# branch
# Created by JKChang
# 21/06/2018, 14:36
# Tag:
# Description: find the branch of the ontology

from owlready2 import *

import os





# for go_concept in onto.classes():
#     print(go_concept.label)
#     for parent in go_concept.is_a:
#         print('  is a %s' %parent.label)


def get_super(onto_class):
    if onto_class.label == '':
        return

    for parent in onto_class.is_a:
        get_super(parent)
        print('  is a %s' % parent.label)

onto = get_ontology('file://./infor.owl').load()

# for go_concept in onto.classes():
#     print(go_concept.label)
#     get_super(go_concept)
#     print('-'*20)

try:
    d = onto.search_one(label = "gala")
    print(d.label)
    print(get_super(d))
except:
    print('can not find xxx')



# gen = onto.classes()
# for i in gen:
#     print(i.label)
#     try:
#         for sub in i.subclasses():
#             print(sub.label)
#     except:
#         pass
#
#     print()
#
# onto.search()


# onto = get_ontology('./infor.owl').load()

# print(onto.name)


