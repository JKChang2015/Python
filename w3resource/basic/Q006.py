# -*- coding: UTF-8 -*-
# Q006
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: input split
# Description: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list
#              and a tuple with those numbers

s = [x for x in input().split(',')]
print(s)
print(tuple(s))
