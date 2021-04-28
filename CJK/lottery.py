# lottery
# Created by JKChang
# 2019-07-08, 10:28
# Tag:
# Description: lottery generator

import random


def set_for_life():
    num = random.sample(range(1, 48), 5)
    star = random.sample(range(1, 11), 1)
    return sorted(num), sorted(star)


def euromillions():
    num = random.sample(range(1, 51), 5)
    star = random.sample(range(1, 13), 2)
    return sorted(num), sorted(star)




a = 0
while (a < 3):
    num, star = euromillions()
    print(num + star)
    a += 1
# a = 0
# while (a<5):
#     num = random.sample(range(1,60),6)
#     print(sorted(num))
#     a += 1


# a = 0
# while (a<5):
#     n = random.randrange(1,6)
#     num = random.sample(range(1,60),n)
#     print(sorted(num))
#     a+=1
