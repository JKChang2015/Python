# Q021
# Created by JKChang
# 27/04/2017, 15:44
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
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

    print 'Distance: ', int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2)))