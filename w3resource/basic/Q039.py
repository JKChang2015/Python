# -*- coding: UTF-8 -*-
# Q039
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: math
# Description: Write a Python program to compute the future value of a specified principal amount, rate of interest,
#              and a number of years.

def future_value(amt, rate, years):
    res = amt * ((1 + (0.01 * rate)) ** years)
    return res


print future_value(1000, 0.1, 10)
