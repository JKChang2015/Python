# prioritySeach
# Created by JKChang
# 14/04/2020, 10:55
# Tag:
# Description: priority search test


class car():
    def __init__(self, age, brand, miles):
        self.age = age
        self.brand = brand
        self.miles = miles


c1 = car(14, 'BMW', 2402)
c2 = car(13, 'AUDI', 2010)
c3 = car(34, 'BENZ', 2931)
c4 = car(23, 'BMW', 3048)

l = [c1, c2, c3, c4]

priority = {'LLJ': 0, 'AUDI': 1}

def setPriority(res_list, priority):
    res = sorted(res_list, key=lambda x: priority.get(x.brand, 1000))
    return res

res = setPriority(l,priority)
for c in res:
    print(c.age, c.brand, c.miles)