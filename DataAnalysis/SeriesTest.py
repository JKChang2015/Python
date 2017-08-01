# -*- coding:utf-8 -*-
# Study
# Created by JKChang
# 27/07/2017, 20:37
# Tag:
# Description: Series testing

from pandas import Series

# x = Series(['a', True, 1])
x = Series([4, 3, 1], index=['1st', '2nd', '3rd'])


print x.values
print '======'
print '1st' in x.index

# x = Series([4, 3, 1], index=['1st', '2nd', '3rd'])

#

# x = x.append(Series([7], index=['info']))
#
# print x
