# _16May
# Created by JKChang
# 16/05/2017, 15:46
# Tag:
# Description: 
import operator

a = ['a', 'b', 'c']
aa = [1, 2, 3, 4, 5]
b = operator.itemgetter(1)
print b
print b(a)  # 'b'
print b(aa)

b = operator.itemgetter(2, 1)
print b(a)
print b(aa)

students = [{'name': 'fang', 'age': 24}, {'name': 'job', 'age': 20}, {'name': 'zen', 'age': 40}]
b = operator.itemgetter('name', 'age')
for i in students:
    print b(i)

students = [{'jack':89}, {'rose':40},{'bils':70}, {'zend':30}]
print
print sorted(students)

print
print sorted(students, key = lambda x:x.keys())

print
print sorted(students, key= lambda x:x.values())