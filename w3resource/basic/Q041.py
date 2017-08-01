# -*- coding: UTF-8 -*-
# Q041
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: check whether a file exists
# Description: Write a Python program to check whether a file exists. 

import os.path

# open('abc.txt', 'w') #creat a file

print((os.path.isfile('abc.txt'))) # check whether a file exists
