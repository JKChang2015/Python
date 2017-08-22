# -*- coding: UTF-8 -*-
# Q020
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: reverse a string
# Description: Write a Python function to reverses a string if it's length is a multiple of 4. 

def func(term):
    if len(term) % 4 == 0:
        return term[::-1]
    return term


print(func('davi'))
print(func('david'))
print(func('davidccc'))
