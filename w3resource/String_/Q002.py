# -*- coding: UTF-8 -*-
# Q002
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: character frequency
# Description: Write a Python program to count the number of characters (character frequency) in a string. 

s = raw_input('please input a string: ')
d = {}
for ch in s:
    if ch.isalpha():
        d[ch] = d.get(ch, 0) + 1

for k, v in d.items():
    print k, v
