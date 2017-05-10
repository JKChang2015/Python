# Q085
# Created by JKChang
# 09/05/2017, 15:37
# Description: Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

li = [5, 6, 77, 45, 22, 12, 24]
l = [x for x in li if x % 2 != 0]
print l
