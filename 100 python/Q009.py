# Q009
# Created by JKChang
# 23/02/2017, 14:39
# Description: Write a program that accepts sequence of lines as input and prints the lines after making all
#              characters in the sentence capitalized.
#
# Example: Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines = []

while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break

for p in lines:
    print p

