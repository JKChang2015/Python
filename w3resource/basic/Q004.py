# -*- coding: UTF-8 -*-
# Q004
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: pi
# Description: Write a Python program which accepts the radius of a circle from the user and compute the area. 

from math import pi
def area(radius):
    return radius **2 * pi

r = float(input('pls input radius of a circle: '))
print(area(r))