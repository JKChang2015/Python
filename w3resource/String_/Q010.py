# -*- coding: UTF-8 -*-
# Q010
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: exchange first& last elements
# Description: Write a Python program to change a given string to a new string where the first and last chars have been
#              exchanged.

def exchange(str1):
    return str1[-1] + str1[1:-1] + str1[0]


str1 = '123456'
print exchange(str1)
