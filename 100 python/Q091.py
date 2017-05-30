# Q091
# Created by JKChang
# 09/05/2017, 15:37
# Tag: intersection
# Description: With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list
#              whose elements are intersection of the above given lists.

l1 = [1, 3, 6, 78, 35, 55]
l2 = [12, 24, 35, 24, 88, 120, 155]
l = [x for x in l1 if x in l2]
print l

# set1 = set([1, 3, 6, 78, 35, 55])
# set2 = set([12, 24, 35, 24, 88, 120, 155])
# set1 &= set2
# li = list(set1)
# print li
