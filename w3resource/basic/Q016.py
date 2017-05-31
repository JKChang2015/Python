# -*- coding: UTF-8 -*-
# Q016
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: difference
# Description: Write a Python program to get the difference between a given number and 17, if the number is greater
#              than 17 return double the absolute difference.

def difference(num):
    if num <= 17:
        return 17 - num
    else:
        return (num - 17) * 2


print difference(14)
print difference(22)
