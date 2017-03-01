# R012
# Created by JKChang
# 01/03/2017, 12:18
# Description: prime number (101,200)

from math import sqrt
from sys import stdout

# --------------------Method 1--------------------------
for num in range(101, 201):
    prime = True
    for pn in range(2, num):
        if (num % pn == 0):
            prime = False
            break
    if prime:
        print num

# --------------------Method 2--------------------------

print '\n\n\n'

h = 0

for nums in range(101, 500):
    leap = True
    k = int(sqrt(nums + 1))
    for i in range(2, k + 1):
        if nums % i == 0:
            leap = False
            break

    if leap:
        print '%-4d' % nums
        h += 1
        if h % 10 == 0:
            print
