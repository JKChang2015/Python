import copy

#deepcopy
will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = copy.deepcopy(will)

print('id of will:', id(will))
for ele in will:
    print('[', ele, ',', id(ele), ']', end=' ')

print('\n')

print('id of wilber', id(wilber))
for ele in wilber:
    print('[', ele, ',', id(ele), ']', end=' ')

print('\n\n')

will[0] = "Wilber"
will[2].append("CSS")
print('id of will:', id(will))
for ele in will:
    print('[', ele, ',', id(ele), ']', end=' ')

print('\n')

print('id of wilber', id(wilber))
for ele in wilber:
    print('[', ele, ',', id(ele), ']', end=' ')