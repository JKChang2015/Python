# Q078
# Created by JKChang
# 09/05/2017, 15:37
# Tag: 
# Description: Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random

print random.sample([i for i in range(100, 201) if i % 2 == 0], 5)
