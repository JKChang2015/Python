# Q072
# Created by JKChang
# 09/05/2017, 15:37
# Description: Please write a binary search function which searches an item in a sorted
#              list. The function should return the index of element to be searched in the list.

import math


def search(list, ele):
    up = len(list)
    low = 0
    while (low <= up):
        index = int(math.floor((up + low) / 2.0))
        if ele == list[index]:
            return index
        elif ele > list[index]:
            low = index + 1
        else:
            up = index - 1
    pass


li = [2, 5, 7, 9, 11, 17, 222]
print search(li, 11)
print search(li, 12)
