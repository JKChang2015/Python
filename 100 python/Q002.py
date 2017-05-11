# Q002
# Created by JKChang
# 16/02/2017, 21:16
# Tag: recursion
# Description: Write a program which can compute the factorial of a given numbers.
#              The results should be printed in a comma-separated sequence on a single line.
#              Suppose the following input is supplied to the program:
#
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x

x = int(raw_input('pls input a number: '))
print fact(x)
