# -*- coding: UTF-8 -*-
# Q051
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: program profile(system performance)
# Description: Write a Python program to determine profiling of Python programs. 
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program
#      executed. These statistics can be formatted into reports via the pstats module.

import cProfile
# 用来衡量系统性能

def sum():
    print((1 + 2))


cProfile.run('sum()')
