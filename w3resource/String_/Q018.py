# -*- coding: UTF-8 -*-
# Q018
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python function to get a string made of its first three characters of a specified string. If the
#              length of the string is less than 3 then return the original string.

def func(term):
    return term[:3] if len(term) > 3 else term


print(func('infor'))
