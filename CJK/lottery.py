# lottery
# Created by JKChang
# 2019-07-08, 10:28
# Tag:
# Description: lottery generator

import random

a = 0
while (a<5):
    num = random.sample(range(1,51),5)
    star = random.sample(range(1,13),2)
    print(sorted(num) + sorted(star))
    a += 1
