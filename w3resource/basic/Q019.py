# -*- coding: UTF-8 -*-
# Q019
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: check string front
# Description: Write a Python program to get a new string from a given string where "Is" has been added to the front.
#              If the given string already begins with "Is" then return the string unchanged.

def new_string(s):
    if len(s) >= 2 and s[:2] == 'Is':
        return s
    else:
        return 'Is' + s


print(new_string("Array"))
print(new_string("IsEmpty"))
