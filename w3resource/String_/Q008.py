# -*- coding: UTF-8 -*-
# Q008
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python function that takes a list of words and returns the length of the longest one. 

# def longest(li):
#     if len(li) == 0:
#         pass
#     else:
#         length = len(li[0])
#         term = li[0]
#         for t in li[1:]:
#             if len(t) > length:
#                 length = len(t)
#                 term = t
#     return term
#
# li = ["PHP", "Exercises", "Backend"]
# print longest(li)

def max_word(l1):
    return max(map(len, l1))


l1 = ["PHP", "Exercises", "Backend"]
print max_word(l1)
