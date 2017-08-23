# -*- coding: UTF-8 -*-
# Q030
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to print the following floating numbers upto 2 decimal places. 
# x = 3.1415926
# y = 12.9999

x = 3.1415926
y = 12.9999

print('{0:.2f}'.format(x))
print('%.2f' % y)

# >> > 125650429603636838 / (2 ** 53)
# 13.949999999999999
#
# >> > 234042163 / (2 ** 24)
# 13.949999988079071
#
# >> > a = 13.946
# >> > print(a)
# 13.946
# >> > print("%.2f" % a)
# 13.95
# >> > round(a, 2)
# 13.949999999999999
# >> > print("%.2f" % round(a, 2))
# 13.95
# >> > print("{0:.2f}".format(a))
# 13.95
# >> > print("{0:.2f}".format(round(a, 2)))
# 13.95
# >> > print("{0:.15f}".format(round(a, 2)))
# 13.949999999999999
