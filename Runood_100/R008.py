# R008
# Created by JKChang
# 01/03/2017, 11:31
# Tag: Times table
# Description: Times Table

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print('%d x %d = ' %(i,j) , j*i, '\t',end= ' ' )
    print()
