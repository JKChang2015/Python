# Q010
# Created by JKChang
# 23/02/2017, 14:44
# Tag: 
# Description: Write a program that accepts a sequence of whitespace separated words as input and prints the words
#              after removing all duplicate words and sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

temp = [x for x in raw_input().split(' ')]

print 'origin:\t', " ".join(temp)

print 'Seted:\t', " ".join(set(temp))

print 'Seted & Sorted:\t', " ".join(sorted(set(temp)))
