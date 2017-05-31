# -*- coding: UTF-8 -*-
# Q021
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: identify even & odd
# Description: Write a Python program to find whether a given number (accept from the user) is even or odd, print out
#              an appropriate message to the user.

def check(num):
    if num % 2 == 0:
        return '%d is a even number' % num
    else:
        return '%d is a odd number' % num


print check(0)
print check(2)
print check(3)
