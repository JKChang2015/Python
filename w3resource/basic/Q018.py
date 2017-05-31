# -*- coding: UTF-8 -*-
# Q018
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: math
# Description: Write a Python program to calculate the sum of three given numbers, if the values are equal then return
#              thrice of their sum.

def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum *= 3
    return sum


print sum_thrice(1, 2, 3)
print sum_thrice(3, 3, 3)
