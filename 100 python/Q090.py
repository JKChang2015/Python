# Q090
# Created by JKChang
# 09/05/2017, 15:37
# Tag: remove particular element
# Description: By using list comprehension, please write a program to print the list after removing the value 24 in
#              [12,24,35,24,88,120,155].

li = [12, 24, 35, 24, 88, 120, 155]
l = [x for x in li if x != 24]
# l = [x for (i, x) in enumerate(li) if x != 24]
print(l)
