# -*- coding: UTF-8 -*-
# File name: studyCount
# Created by JKChang
# 01/07/2020, 20:58
# Tag:
# Description: 

import json
from datetime import timedelta, date
from itertools import accumulate


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2012, 2, 14)
end_date = date.today()
dates = []
for single_date in daterange(start_date, end_date):
    dates.append(single_date)


def MergeDict(d1, d2):
    for year in d2:
        if year not in d1:
            d1.update(d2)
            return d1
        else:
            for month in d2[year]:
                if month not in d1[year]:
                    d1[year].update(d2[year])
                    return d1
                else:
                    for day in d2[year][month]:
                        if day not in d1[year][month]:
                            d1[year][month].update(d2[year][month])
                            return d1
                        else:
                            raise ValueError('Date already exist')


# date1 = datetime(2018, 9, 15)
# date2 = datetime(2018, 9, 16)
# date3 = datetime(2019, 9, 15)
# date4 = datetime(2018, 8, 8)
# date = [date1, date2, date3, date4]
dic = [{x.strftime('%Y'): {x.strftime('%B'): {x.strftime('%d'): 0}}} for x in dates]
r = list(accumulate(dic, MergeDict))[-1]
j = json.dumps(r)
print(j)
