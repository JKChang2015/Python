# -*- coding: UTF-8 -*-
# Q042
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: count char
# Description: Write a python program to count repeated characters in a string.

j = "this is a string"
Dj = {}
for i in sorted(j):
    Dj[i] = j.count(i)
print(Dj)
