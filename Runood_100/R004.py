# R004
# Created by JKChang
# 01/03/2017, 10:31
# Description: Count the days for a certain date.

leap = False

year = raw_input('pls input year')
if year < 0:
    print 'illegal year'
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = True

month = raw_input('pls input month')
if 0 < month <= 12:
    print 'illegal month'

day = raw_input('pls input the day')

