# -*- coding: UTF-8 -*-
# Q005
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: file swap head
# Description: Write a Python program to get a single string from two given strings, separated by a space and swap the
#              first two characters of each string.

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + " " + new_b


print(chars_mix_up('xyz', 'abc'))
