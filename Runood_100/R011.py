# R011
# Created by JKChang
# 01/03/2017, 12:13
# Description: Rabbit problem


f1 = 1
f2 = 1
for i in range(1, 21):
    print '%12ld %12ld' % (f1, f2),
    if (i % 3) == 0:
        print ''
    f1 = f1 + f2
    f2 = f1 + f2
