# R009
# Created by JKChang
# 01/03/2017, 11:41
# Tag: pause one second
# Description: pauses one second

import time

# backwards
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)


# ---------Better -----------

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')

countdown(20)