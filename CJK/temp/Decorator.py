# Decorator
# Created by JKChang
# 04/12/2019, 15:17
# Tag:
# Description: 

from functools import wraps


def deco1(func):
    print('func 1 in')

    def wrapper1():
        print('wrap1 in')
        func()
        print('wrap1 out')

    print('func 1 out')
    return wrapper1


def deco2(func):
    print('func 2 in')

    def wrapper2():
        print('wrap2 in')
        func()
        print('wrap2 out')

    print('func 2 out')
    return wrapper2


@deco1
@deco2
def foo():
    print('foo')


if __name__ == '__main__':
    foo()



# def nameit(fun):
#     @wraps(fun)
#     def wrapper(*args, **kwargs):
#         print('NAME: {name} ...'.format(name= fun.__name__))
#         return fun(*args,**kwargs)
#     return wrapper
#
# def timeing(fun):
#     @wraps(fun)
#     def wrapper(*args, **kw):
#         print('count {name} running time..'.format(name= fun.__name__))
#         start = time()
#         result = fun(*args,**kw)
#         end = time()
#         print('runing time: {time}'.format(time = end-start))
#         return result
#     return wrapper
#
#
# @nameit
# @timeing
# def foo(name):
#     print('hello ' + name)
#
#
# foo('David')
