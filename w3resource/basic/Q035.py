# -*- coding: UTF-8 -*-
# Q035
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: condition return
# Description: Write a Python program that will return true if the two given integer values are equal or their sum or
#              difference is 5.


def dif(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    return False


print dif(1, 1)
print dif(2, 3)
print dif(2, 7)
print dif(6, 1)
print dif(0, 7)
