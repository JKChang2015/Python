# Study
# Created by JKChang
# 27/07/2017, 20:37
# Tag:
# Description: 
from pandas import Series

# x = Series(['a', True, 1])

x = Series(['a', True, 1], index=['1st', '2nd', '3rd'])

x.append(Series(['david'],index =['info']))

print x

