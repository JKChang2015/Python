# Q015
# Created by JKChang
# 31/05/2017, 21:44
# Tag: volume of sphere
# Description: Write a Python program to get the volume of a sphere with radius 6.
# V = 4/3 * pi * (r**3)

from math import pi


def volume(radius):
    return 4 / 3 * pi * (radius ** 3)


r = 6
print volume(6)
