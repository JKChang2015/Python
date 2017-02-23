# Q010
# Created by JKChang
# 23/02/2017, 14:44
# Description: Write a program that accepts a sequence of whitespace separated words as input and prints the words
#              after removing all duplicate words and sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

s = raw_input()
words = [word for word in s.split(' ')]
words = list(set(words))
words.sort()

print " ".join(words)