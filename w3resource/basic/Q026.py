# -*- coding: UTF-8 -*-
# Q026
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: histogram
# Description: Write a Python program to create a histogram from a given list of integers. 

def histogram(l):
    top = max(l)
    while top > 0:
        for i in l:
            if i - top >= 0:
                print('$', end=' ')
            else:
                print(' ', end=' ')
        print()
        top = top - 1


li = [1, 2, 7, 6]
histogram(li)
