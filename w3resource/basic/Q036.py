# -*- coding: UTF-8 -*-
# Q036
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: isinstance, data type
# Description: Write a Python program to add two objects if both objects are an integer type. 

def addd(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return 'inputs should be two integers'


print addd(1, 3)
print addd(1, 'd')
print addd('d', 'a')
