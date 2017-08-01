# Q021
# Created by JKChang
# 27/04/2017, 15:44
# Tag: direction and steps
# Description: The numbers after the direction are steps. Please write a program to compute the distance from current
#              position after a sequence of movement and original point. If the distance is a float, then just print
#              the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math

pos = [0, 0]

while True:
    s = input()
    if not s:
        break

    move = s.split(' ')
    direction = move[0]
    step = int(move[1])
    if direction.upper() == 'UP':
        pos[1] += step
    elif direction.upper() == 'DOWN':
        pos[1] -= step
    elif direction.upper() == 'LEFT':
        pos[0] += step
    elif direction.upper() == 'RIGHT':
        pos[0] -= step
    else:
        pass

    print('Distance: ', int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2))))