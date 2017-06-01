# -*- coding: UTF-8 -*-
# Q046
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: path of the executing file
# Description: Write a python program to get the path and name of the file that is currently executing. 
import os

print "Current File Name : ", os.path.realpath(__file__)
