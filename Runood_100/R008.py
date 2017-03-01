# R008
# Created by JKChang
# 01/03/2017, 11:31
# Description: Times Table

for i in range(1, 10):
    for j in range(1, 10):
        if (i >= j):
            print j, 'x', i, '=', j * i, '\t',
    print
