# -*- coding: UTF-8 -*-
# Q033
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: sum of list
# Description: Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

def s(l):
    if len(set(l)) < len(list(l)):
        return 0
    else:
        return sum(l)


print(s([1, 2, 3, 4]))
print(s([1, 2, 2]))
