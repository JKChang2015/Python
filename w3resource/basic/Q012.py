# Q012
# Created by JKChang
# 31/05/2017, 17:05
# Tag: calender
# Description: Write a Python program to print the calendar of a given month and year.

import calendar

y = int(raw_input('Year: '))
m = int(raw_input('Month: '))
print calendar.month(y,m)

# for i in range (1,13):
#     print calendar.month(y,i)


