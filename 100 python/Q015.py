# Q015
# Created by JKChang
# 28/02/2017, 11:31
# Description: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
# Example: Suppose the following input is supplied to the program:
#           9
#           Then, the output should be:
#           11106


n = raw_input('please input a number between 1 to 9: ')

n1 = int("%s" % n)
n2 = int('%s%s' % (n, n))
n3 = int("%s%s%s" % (n, n, n))
n4 = int("%s%s%s%s" % (n, n, n, n))

print n1, '+', n2, '+', n3, '+', n4, '=', n1 + n2 + n3 + n4
