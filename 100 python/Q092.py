# Q092
# Created by JKChang
# 09/05/2017, 15:37
# Tag: remove duplicate & reversed
# Description: With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing
#              all duplicate values with original order reserved.


def removeDupli(list):
    if len(list) == 0:
        return list
    res = [list[0]]
    for x in list:
        if x not in res:
            res.append(x)
    return res[::-1]

li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDupli(li))
