# -*- coding: UTF-8 -*-
# Q003
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#              If the string length is less than 2, return instead of the empty string.

def func(s):
    if len(s) < 2:
        return ' '
    return s[:2] + s[-2:]


s = input()
print(func(s))
