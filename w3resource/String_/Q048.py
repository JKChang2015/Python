# -*- coding: UTF-8 -*-
# Q048
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to swap comma and dot in a string. 

amount = "32.054,23"
maketrans = amount.maketrans(',.', '.,')
amount = amount.translate(maketrans)
print(amount)

# from string import maketrans   # Required to call maketrans function.
#
# intab = "aeiou"
# outtab = "12345"
# trantab = maketrans(intab, outtab)
#
# str = "this is string example....wow!!!"
# print str.translate(trantab)
