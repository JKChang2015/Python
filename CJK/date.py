# date
# Created by JKChang
# 06/08/2017, 15:53
# Tag:
# Description: 

import datetime

start_date = datetime.date(2017, 3, 4)
print(start_date)

for i in range(20):
    start_date = start_date + datetime.timedelta(28)
    print(start_date)
    i += i
