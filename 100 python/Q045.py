# Q045
# Created by JKChang
# 28/04/2017, 14:59
# Tag: lambda
# Description: Write a program which can filter even numbers in a list by using filter function. The list is:
#              [1,2,3,4,5,6,7,8,9,10]

def filt(li):
    evenNumbers = filter(lambda x: x % 2 == 0, li)
    return evenNumbers


li = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10]
print filt(li)
