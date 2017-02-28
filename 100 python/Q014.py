# Q014
# Created by JKChang
# 28/02/2017, 11:30
# Description: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#
# Example: Suppose the following input is supplied to the program:
#           Hello world!
#           Then, the output should be:
#           UPPER CASE 1
#           LOWER CASE 9

s = raw_input('pls input something:  ')
d = {"UPPER": 0, "LOWER": 0}

for c in s:
    if c.islower():
        d["LOWER"] += 1
    if c.isupper():
        d["UPPER"] += 1
    else:
        pass

print "UPPER", d["UPPER"]
print "LOWER", d["LOWER"]
