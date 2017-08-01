def getAllindex (list,num):
    return [a for a in range(0,len(list)) if list[a]==num]

letters = ['a','b','b','c']
print(getAllindex(letters, 'b'))

