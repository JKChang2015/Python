# fib
# Created by JKChang
# 16/08/2017, 17:01
# Tag:
# Description: 

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def fibs(x):
    for i in range(x):
        print(fib(i), sep='', end=' ', flush=True)


fibs(10)
