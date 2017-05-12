# Q032
# Created by JKChang
# 28/04/2017, 13:53
# Tag: 
# Description: Define a function that can accept an integer number as input and print the "It is an even number" if
#              the number is even, otherwise print "It is an odd number".

def checkValue(num):
    if (num % 2 == 0):
        print '%d is an even number' % num
    else:
        print '%d is an odd number' % num

checkValue(100)
checkValue(101)