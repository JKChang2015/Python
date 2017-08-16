# Q012
# Created by JKChang
# 31/05/2017, 17:05
# Tag: calender
# Description: Write a Python program to print the calendar of a given month and year.

import calendar

year = int(input('pls input the year: '))
month = int(input('pls input the month: '))
# print(calendar.month(year, month))


c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(year,month)


# for i in range(1, 13):
#     print(calendar.month(year, i))
