 # Q60
# Created by JKChang
# 05/05/2017, 09:46
# Tag: 
# Description: Write a program which accepts a sequence of words separated by whitespace as input to print the words
#              composed of digits only.

# Example:
# If the following words is given as input to the program:
#
# 2 cats and 3 dogs.
#
# Then, the output of the program should be:
#
# ['2', '3']
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re
s = raw_input()
print re.findall('\d+', s)
