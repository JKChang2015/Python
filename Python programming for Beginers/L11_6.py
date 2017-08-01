# different combinations of hot dog making

print(' \t\tDog \tBun \tKetchup \tMustard \tOnions')
count = 1
for dog in [0 , 1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onions in [0,1]:
                    print('#', count, '\t', end=' ')
                    print(dog, "\t\t", bun, "\t\t", ketchup, "\t\t\t", mustard, '\t\t\t', onions)
                    count +=1

