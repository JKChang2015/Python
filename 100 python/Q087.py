# Q087
# Created by JKChang
# 09/05/2017, 15:37
# Description: By using list comprehension, please write a program to print the list after removing the
#              0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

li = [12, 24, 35, 70, 88, 120, 155]
l = [x for (i, x) in enumerate(li) if i % 2 != 0]
print l
