# Q037
# Created by JKChang
# 28/04/2017, 14:26
# Tag: 
# Description: Define a function which can generate and print a list where the values are square of numbers
#              between 1 and 20 (both included).

from Q033 import creatDict

d = creatDict(20)
li = []

for key in d.keys():
    li.append(d[key])

print li

