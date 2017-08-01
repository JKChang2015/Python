 # Q60
# Created by JKChang
# 05/05/2017, 09:46
# Tag: re.findall (extract numbers from string)
# Description: Write a program which accepts a sequence of words separated by whitespace as input to print the words
#              composed of digits only.

# Example:
# If the following words is given as input to the program:
#
# # Description: Write a program which accepts a sequence of words separated by whitespace as input to print the words
#              composed of digits only..
#
# Then, the output of the program should be:
#
# ['2', '3']
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

s = input('Inputs: ')
res = [int(x) for x in s.split() if x.isdigit()]
print(res)

#---------The following function can not recognize the digit-string terms, e.g. 3-days----
import re
s = input('Inputs: ')
print(re.findall('\d+', s))

#---------------OUTPUTs----------------------
# Inputs: 2 cats and 3 dogs in 5-days trip
# [2, 3]
# Inputs: 2 cats and 3 dogs in 5-days trip
# ['2', '3', '5']