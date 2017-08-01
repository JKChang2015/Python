# inherit
# Created by JKChang
# 28/04/2017, 11:49
# Description: Inherit

class Person(object):
    def __init__(self,name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == 'male':
            print('Mr', self.name)
        elif self.sex == 'female':
            print('Miss', self.name)
        else:
            pass

class Child(Person):
    def print_title(self):
        if self.sex == 'male':
            print('boy', self.name)
        elif self.sex == 'female':
            print('girl', self.name)
        else:
            pass

May = Child('May','female')
David = Person('David', 'male')

print((May.name, May.sex))
print((David.name, David.sex))

May.print_title()
David.print_title()
