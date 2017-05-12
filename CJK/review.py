# review
# Created by JKChang
# 12/05/2017, 14:10
# Tag:
# Description: use to review the practice



# ----------------Q001-----------------
# Description: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#              between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated
#              sequence on a single line.

# list = []
# for i in range (2000, 3000):
#     if i % 7 ==0 and i% 5!= 0:
#         list.append(str(i))
# print ','.join(list)

# ----------------Q002-----------------
# Description: Write a program which can compute the factorial of a given numbers.
#              The results should be printed in a comma-separated sequence on a single line.
#              Suppose the following input is supplied to the program:

# def fact(x):
#     if x ==0:
#         return 1
#     return fact(x-1) *x
#
# x = int(raw_input())
# print fact(x)

# ----------------Q003-----------------
# Description: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
#              that is an integral number between 1 and n (both included). and then the program should print the
#              dictionary.

# dict = {}
# n = int(raw_input())
# for x in range (1,n+1):
#     dict[x] = x * x
#
# print dict

# ----------------Q004-----------------
# Description: Write a program which accepts a sequence of comma-separated numbers from console and generate a list
#              and a tuple which contains every number.

# seq = '12,23,45,68,21,43,87'
# list = seq.split(',')
# print tuple(list)

# ----------------Q005-----------------
# # Description: Define a class which has at least two methods:
#                getString: to get a string from console input # printString: to print the string in upper case.
#                Also please include simple test function to test the class methods.

# class InOutString(object):
#     def __init__(self):
#         self.str = ''
#
#     def getString(self):
#         self.str = raw_input('input: ')
#
#     def printString(self):
#         print self.str.upper()
#
#
# test = InOutString()
# test.getString()
# test.printString()

# ----------------Q006-----------------
# Description: Write a program that calculates and prints the value according to the given formula:
#                       Q = Square root of [(2 * C * D)/H]
#              Following are the fixed values of C and H: C is 50. H is 30.
#              D is the variable whose values should be input to your program in a comma-separated sequence.

# import math
#
#
# def converter(d):
#     c = 50
#     h = 30
#     return int(round(math.sqrt(2 * c * float(d) / h)))
#
#
# items = [x for x in raw_input().split(',')]
# res = []
# for item in items:
#     res.append(str(converter(int(item))))
#
# print ','.join(res)

# ----------------Q007-----------------
# Description: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element
#              value in the i-th row and j-th column of the array should be i*j.
#              Note: i=0,1.., X-1; j=0,1 !=Y-1.

# dimennsions = [int(x) for x in raw_input('please input rowNum and colNum').split(',')]
# rowNum = dimennsions[0]
# colNum = dimennsions[1]
#
# resArray = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# for row in range(rowNum):
#     for col in range(colNum):
#         resArray[row][col] = row * col
#
# print resArray

# ----------------Q008-----------------
# Description: Write a program that accepts a comma separated sequence of words as input and prints the words in a
#              comma-separated sequence after sorting them alphabetically.

# seq = [ x for x in raw_input().split(',')]
# seq.sort()
# print ','.join(seq)

# ----------------Q009-----------------
# Description: Write a program that accepts sequence of lines as input and prints the lines after making all
#              characters in the sentence capitalized.

line = []
while True:
    s = raw_input()
    if s:
        line.append(s.upper())
    else:
        break

for p in line:
    print p

# ----------------Q010-----------------



# ----------------Q011-----------------



# ----------------Q012-----------------



# ----------------Q013-----------------



# ----------------Q014-----------------



# ----------------Q015-----------------



# ----------------Q016-----------------



# ----------------Q017-----------------



# ----------------Q018-----------------



# ----------------Q019-----------------



# ----------------Q020-----------------



# ----------------Q021-----------------



# ----------------Q022-----------------



# ----------------Q023-----------------



# ----------------Q024-----------------



# ----------------Q025-----------------



# ----------------Q026-----------------



# ----------------Q027-----------------



# ----------------Q028-----------------



# ----------------Q029-----------------



# ----------------Q030-----------------



# ----------------Q031-----------------



# ----------------Q032-----------------



# ----------------Q033-----------------



# ----------------Q034-----------------



# ----------------Q035-----------------



# ----------------Q036-----------------



# ----------------Q037-----------------



# ----------------Q038-----------------



# ----------------Q039-----------------



# ----------------Q040-----------------



# ----------------Q041-----------------



# ----------------Q042-----------------



# ----------------Q043-----------------



# ----------------Q044-----------------



# ----------------Q045-----------------



# ----------------Q046-----------------



# ----------------Q047-----------------



# ----------------Q048-----------------



# ----------------Q049-----------------



# ----------------Q050-----------------



# ----------------Q051-----------------



# ----------------Q052-----------------



# ----------------Q053-----------------



# ----------------Q054-----------------



# ----------------Q055-----------------



# ----------------Q056-----------------



# ----------------Q057-----------------



# ----------------Q058-----------------



# ----------------Q059-----------------



# ----------------Q060-----------------



# ----------------Q061-----------------



# ----------------Q062-----------------



# ----------------Q063-----------------



# ----------------Q064-----------------



# ----------------Q065-----------------



# ----------------Q066-----------------



# ----------------Q067-----------------



# ----------------Q068-----------------



# ----------------Q069-----------------



# ----------------Q070-----------------



# ----------------Q071-----------------



# ----------------Q072-----------------



# ----------------Q073-----------------



# ----------------Q074-----------------



# ----------------Q075-----------------



# ----------------Q076-----------------



# ----------------Q077-----------------



# ----------------Q078-----------------



# ----------------Q079-----------------



# ----------------Q080-----------------



# ----------------Q081-----------------



# ----------------Q082-----------------



# ----------------Q083-----------------



# ----------------Q084-----------------



# ----------------Q085-----------------



# ----------------Q086-----------------



# ----------------Q087-----------------



# ----------------Q088-----------------



# ----------------Q089-----------------



# ----------------Q090-----------------



# ----------------Q091-----------------



# ----------------Q092-----------------



# ----------------Q093-----------------



# ----------------Q094-----------------



# ----------------Q095-----------------



# ----------------Q096-----------------



# ----------------Q097-----------------



# ----------------Q098-----------------



# ----------------Q099-----------------



# ----------------Q100-----------------
