# R010
# Created by JKChang
# 01/03/2017, 11:46
# Description: print current time

import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
