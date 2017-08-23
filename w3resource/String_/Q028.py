# -*- coding: UTF-8 -*-
# Q028
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: insert prefix string
# Description: Write a Python program to add a prefix text to all of the lines in a string.

import textwrap

def func(text, pre):
    res = textwrap.fill(text, width=75)
    res = textwrap.indent(res, prefix=pre)
    return res


sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
print(func(sample_text,'>>> '))


