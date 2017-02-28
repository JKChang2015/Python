# Q015
# Created by JKChang
# 28/02/2017, 11:31
# Description: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
# Example: Suppose the following input is supplied to the program:
#           9
#           Then, the output should be:
#           11106

a = raw_input('Please input a number between 1 to 9:  ')
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
n4 = int("%s%s%s%s" % (a, a, a, a))
print n1, '+', n2, '+', n3, '+', n4, '=', n1 + n2 + n3 + n4
