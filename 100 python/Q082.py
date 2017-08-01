# Q082
# Created by JKChang
# 09/05/2017, 15:37
# Tag: timer
# Description: Please write a program to print the running time of execution of "1+1" for 100 times.

from timeit import Timer

t = Timer("for i in range(100): 1+1")
print(t.timeit())