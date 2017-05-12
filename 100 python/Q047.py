# Q047
# Created by JKChang
# 28/04/2017, 14:59
# Tag: 
# Description: Write a program which can map() and filter() to make a list whose elements are square of even number
#              in [1,2,3,4,5,6,7,8,9,10].

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li))
print result
