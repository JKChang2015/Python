# -*- coding: UTF-8 -*-
# Q029
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: differences of lists
# Description: Write a Python program to print out a set containing all the colors from color_list_1 which are not
#              present in color_list_2.

color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

res = set(color_list_1) - set(color_list_2)
print ','.join(res)
