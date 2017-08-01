# test cpy progress

# assigning
will = ['will', 28, ['Python', 'C#', 'JavaScript']]
wilber = will[:]

print('id of will:', id(will))
for ele in will:
    print('[', ele, ',', id(ele), ']', end=' ')

print('\n')

print('id of wilber', id(wilber))
for ele in wilber:
    print('[', ele, ',', id(ele), ']', end=' ')

print('\n\n')

#------------make some changes---------
will[1] = 1001
will[2].append('information')
print('id of will:', id(will))
for ele in will:
    print('[', ele, ',', id(ele), ']', end=' ')

print('\n')

print('id of wilber', id(wilber))
for ele in wilber:
    print('[', ele, ',', id(ele), ']', end=' ')


