# -*- coding: UTF-8 -*-
# Q019
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: right split
# Description: Write a Python program to get the last part of a string before a specified character. 

s = 'http://www.google.co.uk/map/direction'
res = s.rsplit('/', 1)[0]
print(res)

res = s.split('/', 1)[0]
print(res)
