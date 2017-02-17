numBlock = int(raw_input('How many blocks do you want: '))
numLine = int(raw_input('How many lines of stars do you want: '))
numStar = int(raw_input('How many stars per line? '))
for block in range(numBlock):
    for line in range(numLine):
        for star in range(numStar):
            print "*",
        print
    print "\n"