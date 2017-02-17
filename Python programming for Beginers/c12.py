list = ['a', 'b', 'c']
print list.index('a')
print list.index('b')

letter = raw_input('pls input a letter: ')
if letter in list:
    print 'Yes', letter, 'is in the list: ' ,list
else:
    print 'No', letter, 'is not in the list'





# list = [ 'a' , 'b' , 'c' , 'e']
# list.append('f')
# print 'append: ', list
#
# list = [ 'a' , 'b' , 'c' , 'e']
# list.extend(['f', 'm', 'n'])
# print 'extend: ', list
#
# list = [ 'a' , 'b' , 'c' , 'e']
# list.insert(3, 'd')
# print 'insert: ', list

# list = [ 'a' , 'b' , 'c' , 'e']
# list.append(['f', 'f', 'f'])
# print list