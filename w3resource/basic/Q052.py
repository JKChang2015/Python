# -*- coding: UTF-8 -*-
# Q052
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: 
# Description: Write a Python program to print to stderr. 


from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

