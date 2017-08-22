# -*- coding: UTF-8 -*-
# Q016
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: insert into string
# Description: Write a Python function to insert a string in the middle of a string. 

def func(term1, term2):
    mid = int(len(term1) / 2)
    res = term1[:mid] + term2 + term1[mid:]
    return res


print(func('hahaa', 'xo' * 3))
