# -*- coding: UTF-8 -*-
# File name: ukWorkingDays
# Created by JKChang
# 29/07/2020, 11:20
# Tag:
# Description:

from datetime import date,timedelta,datetime
from workalendar.europe import UnitedKingdom

cal = UnitedKingdom()
print(cal.holidays(2020))

def workingDate(start,end):
    cal = UnitedKingdom()
    res = []
    delta = end - start
    for i in range(delta.days +1):
        day = start + timedelta(days=i)
        if cal.is_working_day(day) or day.weekday() < 5:
            res.append(day)
        else:
            pass
    return res

start = datetime.today()
end = datetime(2020, 12, 23)
r = workingDate(start,end)
for d in r:
    print(d.strftime('%d-%B-%Y'))
    print('\n'*3)
