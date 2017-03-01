# R009
# Created by JKChang
# 01/03/2017, 11:41
# Description: pauses one second

import time

flu = {1: 'a', 2: 'b'}

# loop for the dict
for key, value in dict.items(flu):
    print key, value
    time.sleep(1)

# backwards
for i in range(10, 0 , -1):
    print i
    time.sleep(1)

