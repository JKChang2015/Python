# Index_Example
# Created by JKChang
# 15/08/2017, 09:13
# Tag:
# Description: 

# print out a date, give a year, month and day as number

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

# A list with one ending for each number from 1 to 31

endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

year = input('Year: ')
month = int(input('Month: '))
day = input('Day: ')

print(day + endings[int(day) - 1], months[month - 1], year)


