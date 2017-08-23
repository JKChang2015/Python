# Q22
# Created by JKChang
# 22/08/2017, 17:12
# Tag: sorted with two keys
# Description: Write a Python program to sort a string lexicographically.

def func(term):
    # first sort upper case, then lower case
    res = sorted(term, key=lambda element: (str.upper(element), element))
    return res


s = 'aaBbcCAdE'
print(func(s))
