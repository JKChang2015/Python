# -*- coding: UTF-8 -*-
# Q025
# Created by JKChang
# Tag: class parameter & instance parameter
# 28/04/2017, 11:16
# Description:  Define a class, which have a class parameter and have a same instance parameter.

class Person(object):
    # Define the class parameter 'name'
    # 类变量类似于静态变量 只属于类不属于对象
    name = 'someone'

    def __init__(self, n=None):
        self.name = n


dav = Person('David')
print 'dav name:', dav.name
print 'Person name: ', Person.name

Person.name = 'Chan'
print 'change Person name:', Person.name

dove = Person('Dove')
print 'dove name: ', dove.name
print 'Person name: ', Person.name
