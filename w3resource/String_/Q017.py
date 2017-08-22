# -*- coding: UTF-8 -*-
# Q017
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: copy part of string
# Description: Write a Python function to get a string made of 4 copies of the last two characters of a specified string
#              (length must be at least 2).

def func(term):
    if len(term) < 2:
        raise TypeError('len of term must be more than 2')
    return term[-2:] * 4


print(func('xin'))
