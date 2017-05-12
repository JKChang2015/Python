# Q038
# Created by JKChang
# 28/04/2017, 14:26
# Tag: 
# Description: Define a function which can generate a list where the values are square of numbers between 1 and 20 (
#              both included). Then the function needs to print the first 5 elements in the list.

from Q033 import creatDict

d = creatDict(20)
li = []

for key in d.keys():
    li.append(d[key])

print li[:5]