# -*- coding: utf-8 -*-
# 2Darray
# Created by JKChang
# 23/02/2017, 13:41
# Description: Test 2-Dimensional Array

# 一维数组
array = [0, 0, 0]
print array

# 简单的相乘 让数组变得更长, (一次改变单个值）
matrix = array * 3
print matrix
matrix[5] = 2
print matrix

# 加括号相乘
matrix2 = [array * 3]
print matrix2

matrix3 = [array] * 3
print matrix3

matrix3[0][1] = 2
print matrix3

matrix4 = [[0 for i in range(3)] for j in range(3)]
print matrix4

matrix4[0][1] = 2
print matrix4
