# -*- coding:UTF-8 -*-
# Q094
# Created by JKChang
# Tag: 
# 09/05/2017, 15:37
# Description: Please write a program which count and print the numbers of each character in a string input by console.

# Example:
# If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

s = raw_input('please input something: ').strip()
dit = {}

for i in s:
    dit[i] = dit.get(i, 0) + 1  # 返回指定键的值，如果值不在字典中返回default值

print '\n'.join(['%s,%s' % (k, v) for k, v in dit.items()])
