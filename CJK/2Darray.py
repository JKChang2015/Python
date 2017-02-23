# -*- coding: utf-8 -*-
# 2Darray
# Created by JKChang
# 23/02/2017, 13:41
# Description: Test 2-Dimensional Array

# 一维数组
array = [0, 0, 0]
print array

print '--------------------'

# 简单的相乘 让数组变得更长, (一次改变单个值）
matrix = array * 3
print matrix
matrix[5] = 2
print matrix

print '--------------------'

# 加括号相乘 数组成为列数为1 的变长的二维数组 （一次改变单个值）
matrix2 = [array * 3]
print matrix2
matrix2[0][3] = 2
print matrix2

print '--------------------'

# 先将原数组变成2维， 然后相乘， 会变成2维数组
# 一个改变全部改变 （类似于普通copy
matrix3 = [array] * 3
print matrix3
matrix3[1][1] = 1
matrix3[2][2] = 2
print matrix3

print '--------------------'

# 正确的方式初始化一个数组，分别赋值，'0' 既是初始值
matrix4 = [[0 for i in range(3)] for j in range(3)]
print matrix4

matrix4[0][1] = 2
print matrix4
