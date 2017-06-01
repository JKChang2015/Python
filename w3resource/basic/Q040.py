# -*- coding: UTF-8 -*-
# Q040
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: distance of two points
# Description: Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 

import math


def distance(point1, point2):
    if len(point1) > 2 or len(point2) > 2:
        pass
    x = (float(point1[0]) - float(point2[0])) ** 2
    y = (float(point1[1]) - float(point2[1])) ** 2
    return math.sqrt(x + y)


print distance((4, 0), (6, 6))
