# test cpy progress

# assiging
will = ['will', 28, ['Python', 'C#', 'JavaScript']]
wilber = will[:]

print 'id of will:', id(will)
for ele in will:
    print '[', ele, ',', id(ele), ']',

print '\n'

print 'id of wilber', id(wilber)
for ele in wilber:
    print '[', ele, ',', id(ele), ']',

print '\n\n'

#------------make some changes---------
will[1] = 1001
print 'id of will:', id(will)
for ele in will:
    print '[', ele, ',', id(ele), ']',

print '\n'

print 'id of wilber', id(wilber)
for ele in wilber:
    print '[', ele, ',', id(ele), ']',


