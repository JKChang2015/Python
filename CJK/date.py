# date
# Created by JKChang
# 06/08/2017, 15:53
# Tag:
# Description: calculate date for a certain period

import datetime

start_date = datetime.date(2017, 3, 4)
print(start_date)

for i in range(30):
    start_date = start_date + datetime.timedelta(28)
    print(start_date)
    i += i
