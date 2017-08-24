# -*- coding: UTF-8 -*-
# Q050
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: rsplit
# Description: Write a Python program to split a string on the last occurrence of the delimiter. 
str1 = "In/f/orm/atio/n re/triev/al"
print(str1.rsplit('/', 1))
print(str1.rsplit('/', 2))
print(str1.rsplit('/', 5))