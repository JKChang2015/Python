# tt
# Created by JKChang
# 10/03/2018, 13:56
# Tag:
# Description: 

def fib3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

print(fib3(10))