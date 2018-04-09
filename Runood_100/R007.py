# R007
# Created by JKChang
# 01/03/2017, 11:30
# Tag: copy list
# Description: copy the list ( copy and deep-cooy)

a = [1, 2, 3, 3]
b = a[:]
a = [1,2]
print(b)

a = [1, 2, 3, 3]
c = a.copy()
a = [1,2]
print(c)