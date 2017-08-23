# -*- coding: UTF-8 -*-
# Q021
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: change char case
# Description: Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase
#              characters in the first 4 characters.

def func(term):
    up = [x for x in term[:4] if x.isupper()]
    if len(up) >= 2:
        return term.upper()
    else:
        return term


print(func('Python'))
print(func('PyThon'))
