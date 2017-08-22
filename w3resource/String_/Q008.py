# -*- coding: UTF-8 -*-
# Q008
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: list map
# Description: Write a Python function that takes a list of words and returns the length of the longest one. 

# 1
def longest(l):
    if len(l) <= 1:
        return l
    maxlength = 0
    res = ' '
    for term in l:
        if len(term) >= maxlength:
            maxlength = len(term)
            res = term
    print(res, maxlength)


l1 = ["PHP", "Exercises", "Backend"]

# 2
res = sorted(l1, key=lambda x: len(x))[-1]
print(res)

# l1.sort(key=lambda x: len(x))
# print(l1)
# longest(l1)
