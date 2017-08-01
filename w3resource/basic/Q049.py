# -*- coding: UTF-8 -*-
# Q049
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: list of file in directory
# Description: Write a Python program to list all files in a directory in Python. 
from os import listdir
from os.path import isfile, join

import os

print('\n'.join(os.listdir('/Users/jkchang/Github/Python/w3resource/basic/')))