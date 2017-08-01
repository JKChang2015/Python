numBlock = int(input('How many blocks do you want: '))
numLine = int(input('How many lines of stars do you want: '))
numStar = int(input('How many stars per line? '))
for block in range(numBlock):
    for line in range(numLine):
        for star in range(numStar):
            print("*", end=' ')
        print()
    print("\n")