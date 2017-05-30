# -*- coding: UTF-8 -*-
# R003
# Created by JKChang
# 01/03/2017, 09:53
# Tag: conditional
# Description: 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

import math

for i in range(10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))

    if (x ** 2 == i + 100) and (y * y == i+268):
        print x, y
        print i

