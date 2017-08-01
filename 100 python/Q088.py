# Q088
# Created by JKChang
# 09/05/2017, 15:37
# Tag: multi-Dimensional array
# Description: By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[[0 for col in range(8)] for co in range(5)] for c in range(3)]
print(array)