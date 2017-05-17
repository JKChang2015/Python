# Q048
# Created by JKChang
# 28/04/2017, 15:00
# Tag: filter and lambda
# Description: Write a program which can filter() to make a list whose elements are even number between 1 and 20
#              (both included).

print filter(lambda x: x % 2 == 0, range(1, 21))
