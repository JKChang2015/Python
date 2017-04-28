# Q025
# Created by JKChang
# 28/04/2017, 11:16
# Description:  Define a class, which have a class parameter and have a same instance parameter.

class Person(object):
    # Define the class parameter 'name'
    name = 'Someone'

    def __init__(self, n=None):
        self.name = n





dav = Person("David")
print dav.name

chan = Person()
print chan.name
