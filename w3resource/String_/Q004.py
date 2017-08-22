# -*- coding: UTF-8 -*-
# Q004
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: replace char
# Description: Write a Python program to get a string from a given string where all occurrences of its first char have
#              been changed to '$', except the first char itself.

# Sample String : 'restart'
# Expected Result : 'resta$t'

s = input()
res = s[1:].replace(s[0],'$')
print(s[0]+res)
