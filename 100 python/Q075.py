# Q075
# Created by JKChang
# 09/05/2017, 15:37
# Tag: 
# Description: Please write a program to output a random even number between 0 and 10 inclusive using random module
#              and list comprehension.

import random

print random.choice([i for i in range(11) if i%2==0])