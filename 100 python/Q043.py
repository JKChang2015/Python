# Q043
# Created by JKChang
# 28/04/2017, 14:59
# Tag: 
# Description: Write a program to generate and print another tuple whose values are even numbers in the given
#              tuple (1,2,3,4,5,6,7,8,9,10).

def printTuple(tu):
    print tu[1::2]

tu = (1,2,3,4,5,6,7,8,9,10)
printTuple(tu)