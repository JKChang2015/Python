# -*- coding: UTF-8 -*-
# Q004
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to get a string from a given string where all occurrences of its first char have
#              been changed to '$', except the first char itself.

# Sample String : 'restart'
# Expected Result : 'resta$t'

s = raw_input('please input something')
res = s[1:].replace(s[0], '$')
print res
