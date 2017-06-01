# -*- coding: UTF-8 -*-
# Q027
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: random digits and letters
# Description: Write a Python program to concatenate all elements in a list into a string and return it. 

import random
import string
from random import sample

li = sample(range(10), 5)
le = sample(string.letters, 5)
l = li + le
random.shuffle(l)
print ''.join([str(x) for x in l])
