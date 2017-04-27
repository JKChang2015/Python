# Q020
# Created by JKChang
# 28/02/2017, 11:39
# Description: Define a class with a generator which can iterate the numbers, which are divisible by 7,
#              between a given range 0 and n.

def Genert(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j

for i in Genert(1000):
    print i
