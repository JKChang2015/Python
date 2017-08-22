# -*- coding: UTF-8 -*-
# Q006
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: conditional
# Description: Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#              If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
#              string is less than 3, leave it unchanged.

def change(term):
    if len(term) < 3:
        return term
    if term[-3:] == 'ing':
        return term + 'ly'
    else:
        return term + 'ing'


s = ['sleep', 'interesting', 'OK']
for i in s:
    print(change(i))




# def change(term):
#     if len(term) < 3:
#         return term
#     if term[-3:] == 'ing':
#         return term + 'ly'
#     else:
#         return term + 'ing'
#
#
# s = ['sleep', 'interesting', 'OK']
# for i in s:
#     print(change(i))
