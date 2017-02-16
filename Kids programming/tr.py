import copy

origin = ['a', 2, 'Java']
cpy = copy.copy(origin)

print 'id of origin:', id(origin)
for ele in origin:
    print '[', ele, ',', id(ele), ']',

print '\n'

print 'id of cpy', id(cpy)
for ele in cpy:
    print '[', ele, ',', id(ele), ']',

print '\n\n origin is cpy: ',origin is cpy

origin[1] = 1112
print origin
print cpy





#
#
# print 'origin is cpy: ',origin is cpy
#
# origin = ('a', 8, 'Java', [1,2,3,4])
# cpy = copy.deepcopy(origin)
# print 'origin is cpy: ',origin is cpy


