# -*- coding:UTF-8 -*-
# Q071
# Created by JKChang
# Tag: eval
# 09/05/2017, 15:37
# Description: Please write a program which accepts basic mathematic expression from console and print the evaluation
#              result.

# Example:
# If the following string is given as input to the program:
#
# 35+3
#
# Then, the output of the program should be:
# 38

#将字符串str当成有效的表达式来求值并返回计算结果。其他用法，可以把list,tuple,dict和string相互转化

s = raw_input('please input: ')
print eval(s)