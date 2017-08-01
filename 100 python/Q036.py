# Q036
# Created by JKChang
# 28/04/2017, 14:26
# Tag: dictionary keys
# Description: Define a function which can generate a dictionary where the keys are numbers between 1 and 20
#              (both included) and the values are square of keys. The function should just print the keys only.

from .Q033 import creatDict

d = creatDict(20)
print(list(d.keys()))