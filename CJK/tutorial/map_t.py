# map_t
# Created by JKChang
# 2019-08-01, 10:18
# Tag:
# Description: 

def add(x,y,z):
    return x,y,z

l1 = [1,2,3]
l2 = [3,2]
l3 = [1,1,1,1]

res = map (add,l1,l2,l3)

for x in res:
    print(x)