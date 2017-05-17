# Q042
# Created by JKChang
# 28/04/2017, 14:59
# Tag: tuple subtraction
# Description: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
#              and the last half values in one line.

def printValue(tu):
    print tu[:len(tu) / 2]
    print tu[len(tu) / 2:]


tu = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
printValue(tu)
