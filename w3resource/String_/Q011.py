# -*- coding: UTF-8 -*-
# Q011
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: remove odd index
# Description: Write a Python program to remove the characters which have odd index values of a given string. 

s = input()
res = ''
for i in range(len(s)):
    if i % 2 != 0:
        res = res + s[i]

print(res)
