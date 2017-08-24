# -*- coding: UTF-8 -*-
# Q047
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to lowercase first n characters in a string. 

def func(term, n):
    return term[:n].lower() + term[n:]


print(func('DAviD3', 4))
