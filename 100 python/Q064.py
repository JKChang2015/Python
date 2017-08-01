# Q064
# Created by JKChang
# 09/05/2017, 14:31
# Tag: math
# Description: Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 3.55
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

n = int(input('Please input a integer: '))
s = 0


for i in range (1, n + 1):
    s += float(float(i)/(i+1))

print(s)
