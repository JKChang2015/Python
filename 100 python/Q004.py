# Q004
# Created by JKChang
# 16/02/2017, 21:22
# Tag: tuple, string split
# Description: Write a program which accepts a sequence of comma-separated numbers from console and generate a list
#              and a tuple which contains every number.
#
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

seq = '12,23,45,68,21,43,87'
list = seq.split(',')
tuple = tuple(list)

print list
print tuple
