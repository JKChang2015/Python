# -*- coding: UTF-8 -*-
# Q050
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: print without newline
# Description: Write a Python program to print without newline or space. 

import sys

# for i in xrange(20):
#    sys.stdout.write('a')

for i in range(15):
    print('\b*', end=' ')