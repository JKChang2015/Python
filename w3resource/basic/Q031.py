# -*- coding: UTF-8 -*-
# Q031
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: greatest common divisor (GCD)
# Description: Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


# print gcd(4, 20)
# print gcd(20, 4)
# print gcd(3, 11)
