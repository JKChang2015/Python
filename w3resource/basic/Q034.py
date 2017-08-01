# -*- coding: UTF-8 -*-
# Q034
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: sum
# Description: Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def s(a, b):
    res = a + b
    if res > 15 and res < 20:
        return 20
    return res


print(s(7, 9))
print(s(10, 3))
print(s(12, 43))
