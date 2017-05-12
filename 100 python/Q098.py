# Q098
# Created by JKChang
# 09/05/2017, 15:37
# Tag: 
# Description: Write a program to solve a classic ancient Chinese puzzle:
#              We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many
#              chickens do we have?

def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return 'No solutions!'


numheads = 35
numlegs = 94
solutions = solve(numheads, numlegs)
print solutions
