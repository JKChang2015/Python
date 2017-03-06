# R014
# Created by JKChang
# 01/03/2017, 14:31
# Description: prime factorization



def pFact(n):
    if not isinstance(n, int) or n <= 0:
        print 'Please input a integer'
        exit(0)
    elif n in [1]:
        print