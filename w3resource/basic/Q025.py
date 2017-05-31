# -*- coding: UTF-8 -*-
# Q025
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: is_in_group_member
# Description: Write a Python program to check whether a specified value is contained in a group of values. 

def check(num, group):
    return num in group


li = [1, 2, 34, 5]
print check(4, li)
print check(2, li)
