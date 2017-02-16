def getAllindex (list,num):
    return filter(lambda a: list[a]==num, range(0,len(list)))

letters = ['a','b','b','c']
print getAllindex(letters, 'b')

