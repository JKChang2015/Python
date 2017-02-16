import copy

origin = ('a', 'in', 'Java')
cpy = copy.deepcopy(origin)
print 'origin is cpy: ',origin is cpy

origin = ('a', 8, 'Java', [1,2,3,4])
cpy = copy.deepcopy(origin)
print 'origin is cpy: ',origin is cpy


