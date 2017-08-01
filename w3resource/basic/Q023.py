# -*- coding: UTF-8 -*-
# Q023
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: repeat first 2 char
# Description: Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given
#              string. Return the n copies of the whole string if the length is less than 2.

def copy(st, num):
    if len(st) <= 2:
        return st * num
    else:
        return st[:2] * num


print(copy('hi', 5))
print(copy('hello', 4))
