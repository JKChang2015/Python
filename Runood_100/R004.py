# R004
# Created by JKChang
# 01/03/2017, 10:31
# Tag: Date count
# Description: Count the days for a certain date.

def monthDay(month):
    swithcher = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return swithcher.get(month)


res = 0

leap = False
year = int(input('pls input year: '), )
if year < 0:
    print('illegal year')
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = True

month = int(input('pls input month: '), )
if (month < 0) or (month > 12):
    print('illegal month')

for mon in range(1, month):
    res += monthDay(mon)

day = int(input('pls input the day: '), )
res += day

if (month > 2) and leap:
    res += 1

print('it is the %dth day.' % res)
