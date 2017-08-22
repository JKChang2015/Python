# -*- coding: UTF-8 -*-
# Q014
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program that accepts a comma separated sequence of words as input and prints the
#              unique words in sorted form (alphanumerically).

s = input('pls input terms seaprated by comma:  ').split(',')
res = sorted(list(set(s)))
print(','.join(res))
