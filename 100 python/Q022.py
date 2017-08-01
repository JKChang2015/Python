# Q022
# Created by JKChang
# 27/04/2017, 16:11
# Tag: sorting dictionary
# Description: Write a program to compute the frequency of the words from the input. The output should output after
#              sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

import operator

freq = {}
line = input()

for word in line.split(" "):
    freq[word] = freq.get(word, 0) + 1  # add 1, if not existed, creat one and add 1

print('dictionary: ', freq)
# sorted according to the term frequency (values)
freq1 = sorted(list(freq.items()), key=operator.itemgetter(1))
print(type(freq1))

print('sorted according to the term frequency (values): ', freq1)

# sorted according to the alphabetical (keys)
freq2 = sorted(list(freq.items()), key=operator.itemgetter(0))
print('sorted according to the alphabetical (keys) : ', freq2)
