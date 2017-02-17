# Q002
# Created by JKChang
# 16/02/2017, 21:16
# Description: Write a program which can compute the factorial of a given numbers.
#              The results should be printed in a comma-separated sequence on a single line.
#              Suppose the following input is supplied to the program:

def fact(x):
    if x == 0:
        return 1;
    return x * fact(x - 1)


x = int(raw_input('pls input a number: '))
print fact(x)
