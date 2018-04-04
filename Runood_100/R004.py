# R004
# Created by JKChang
# 01/03/2017, 10:31
# Tag: Date count
# Description: Count the days for a certain date.

from datetime import datetime

now = datetime.now()
new_year = now.replace(month=1, day=1)
delta = (now - new_year).days
print(delta)
