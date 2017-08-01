# -*- coding: UTF-8 -*-
# Q032
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: least common multiple (LCM)
# Description: Write a Python program to get the least common multiple (LCM) of two positive integers. 

from Q031 import gcd


def lcm(x, y):
    return (x * y) / gcd(x, y)


print(lcm(54, 24))
