# Q003
# Created by JKChang
# 31/05/2017, 16:27
# Tag: date & time
# Description: 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%s'))
print(now.strftime('%D'))

# %Y Year with century as a decimal number.	1970, 1988, 2001, 2013
# %y Year without century as a zero-padded decimal number.	00, 01, ..., 99
# %M Minute as a zero-padded decimal number.	00, 01, ..., 59
# %m Month as a zero-padded decimal number.	01, 02, ..., 12%
# %D month/day/year 05/31/17
# %d Day of the month as a zero-padded decimal number.	01, 02, ..., 31
# %H Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
# %h -
# %S Second as a zero-padded decimal number.	00, 01, ..., 59
# %s -
