# L13_global
# Created by JKChang
# 20/02/2017, 15:58
# Description: 

x = 50


def func():
    global x
    print'x=', x

    x = 2
    print'local change to:', x


func()
print'x = ', x
