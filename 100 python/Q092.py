# Q092
# Created by JKChang
# 09/05/2017, 15:37
# Description: With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing
#              all duplicate values with original order reserved.


def removeDupli(list):
    if len(list) == 0:
        pass
    else:
        newList = [list[0]]
        for i in list:
            if i in newList:
                continue
            else:
                newList.append(i)
        return newList

li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print removeDupli(li)
