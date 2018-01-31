# Ch4
# Created by JKChang
# 07/01/2018, 13:20
# Tag:
# Description: List operation

# ----------------FOR loop ---------------------
pizzas = ['pizza1', 'pizza2', 'pizza3']
for pizza in pizzas:
    print(pizza)

print()
animals = ['Elephant', 'Kangaroo', 'Giraffe']
for x in animals:
    print(x, 'is a good pet')
print('Any of them are good')

# ------------------range()----------------------
print()
for x in range(1, 21):
    print(x, end=' ')

# print()
# for x in range(1, 1000001):  # print 1- 1000000
#     print(x)

print('\n')
l = [x for x in range(1, 101)]
print(sum(l))

# odd number
print('\nodd number from 1 to 20: ')
odd_num = [x for x in range(1, 21) if x % 2 != 0]
for num in odd_num:
    print(num, end=' ')

# multiple
print('\nmultiple value of 3 in range 3-30: ')
three = [x for x in range(3, 31) if x % 3 == 0]
for num in three:
    print(num, end=' ')

# power
print('\ncube value in 1 to 10: ')
pw = [x ** 3 for x in range(1, 11)]
for num in pw:
    print(num, end=' ')

# Cut'the first three items of the list is: ' + ','.join(l[:3]))
print('\n')
l = [str(x) for x in range(1,10)]
print('the first three items of the list is: ' + ','.join(l[:3]))
print('the middle items of the list is: ' + ','.join(l[len(l)//2-1:len(l)//2+2]))
print('the last three items of the list is: ' + ','.join(l[-3:]))

