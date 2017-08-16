# args_test
# Created by JKChang
# 16/08/2017, 20:11
# Tag:
# Description: 


# 这四种方法优先级依次降低，先1，后2，再3，最后4
# ------------------------------------------
# 数量一定，相对位置一定
def F1(x, y):
    print(x, y)


F1(2, 3)  # 2 3


# ------------------------------------------
# 数量一定，相对位置一定，默认值变量名固定
def F2(x, y=5):  # default value, y =5
    print(x, y)


F2(2, 3)  # 2 3
# F1(2,a=3)  错误，变量必须为y
F2(2)  # 2 5


# ------------------------------------------
# 数量任意，变量以tuple形式存储
def F3(*x):
    if len(x) == 0:
        print(None)
    elif len(x) == 1:
        print('Single value = ', x[0])
    else:
        s = 0
        for ele in x:
            s += ele
        print(s)


F3()  # None
F3(1)  # Single value = 1
F3(2, 3)  # 5
F3(1, 2, 3, 4)  # 10


# ------------------------------------------
# 数量任意，变量名任意，以dict形式存储
def F4(**x):
    if len(x) == 0:
        print(None)
    else:
        print(x)


F4()  # None
F4(x=1, y=12)  # {'x': 1, 'y': 12}


# -----------test ---------------

def test(x, y=1, *a, **b):
    print(x, y, a, b)


test(1)  # 1 1 () {}
test(1, 2)  # 1 2 () {}
test(1, 2, 3)  # 1 2 (3,) {}
test(1, 2, 3, 4)  # 1 2 (3,4) {}
test(1, 2, 3, 4, 5)  # 1 2 (3,4,5) {}

test(x=1, y=2)  # 1 2 () {}
test(1, y=2)  # 1 2 () {}
test(1, a=2)  # 1 1 () {'a': 2}
test(1, 3, 3, 4, c=6)
test(1, 3, 4, 5, c=6, d=7, f=8)


def test2(x=1, *y):
    print(x, y)


test2(2)
test2(4, 3, 4, 5, 6)
