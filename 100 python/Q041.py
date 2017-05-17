# Q041
# Created by JKChang
# 28/04/2017, 14:59
# Tag: list to tuple
# Description: Define a function which can generate and print a tuple where the value are square of numbers between 1
#              and 20 (both included).

from Q033 import creatDict

d = creatDict(20)
li = []

for key in d.keys():
    li.append(d[key])


print tuple(li)