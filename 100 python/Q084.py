# Q084
# Created by JKChang
# 09/05/2017, 15:37
# Tag: combinations
# Description: Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play"
#              , "Love"] and the object is in ["Hockey","Football"].

import itertools

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

c = list(itertools.product(subjects, verbs, objects))
for i in c:
    for j in i:
        print j,
    print

# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
#             print sentence
