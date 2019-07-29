# lottery
# Created by JKChang
# 2019-07-08, 10:28
# Tag:
# Description: lottery generator

import random

# a = 0
# while (a<7):
#     num = random.sample(range(1,39),5)
#     star = random.sample(range(1,14),1)
#     print(sorted(num) + sorted(star))
#     a += 1


# a = 0
# while (a<5):
#     num = random.sample(range(1,60),6)
#     print(sorted(num))
#     a += 1


a = 0
while (a<5):
    n = random.randrange(1,6)
    num = random.sample(range(1,60),n)
    print(sorted(num))
    a+=1

