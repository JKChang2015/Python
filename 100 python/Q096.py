# Q096
# Created by JKChang
# 09/05/2017, 15:37
# Tag: even elements of list
# Description: Please write a program which accepts a string from console and print the characters that have even indexes.

# Example:even index
# If the following string is given as input to the program:
#
# H1e2l3l4o5w6o7r8l9d
#
# Then, the output of the program should be:
#
# Helloworld
#

s = input('input: ')
print(s[::2])
