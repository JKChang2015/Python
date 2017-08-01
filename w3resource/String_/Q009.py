# -*- coding: UTF-8 -*-
# Q009
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: remove nth index character
# Description: Write a Python program to remove the nth index character from a nonempty string. 

def remove_ch(st,index):
    return st[:index-1] + st[index:]

st = 'abcdefg'
print(remove_ch(st,2))

num = '123456'
print(num[:2] ,num[2:])