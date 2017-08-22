# -*- coding: UTF-8 -*-
# Q012
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: word frequency
# Description: Write a Python program to count the occurrences of each word in a given sentence. 

def count(s):
    se = s.split(' ')
    d = {}
    for word in se:
        d[word] = d.get(word, 0) + 1
    return d


i = input()
d = count(i)
for k, v in d.items():
    print(k, v)

