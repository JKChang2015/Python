# R006
# Created by JKChang
# 01/03/2017, 11:13
# Tag: Fibonacci sequence
# Description: Fibonacci sequence

def fib(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


for i in range(1, 10):
    print(fib(i))
