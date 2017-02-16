origin = [ 'Tom', 'Amy', 'David', 'Matt', 'Dave']
newSort1 = origin[:]
newSort2 = origin[:]

newSort1.sort()
newSort2.sort(reverse=True)

print 'origin: ', origin
print 'sorted: ', newSort1
print 'reverse sorted: ', newSort2
