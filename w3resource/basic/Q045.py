# -*- coding: UTF-8 -*-
# Q045
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: call external command
# Description: Write a python program to call an external command in Python. 
from subprocess import call

call(["ls", "-l"])  # -l     use a long listing format
