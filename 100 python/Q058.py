# Q058
# Created by JKChang
# 05/05/2017, 09:45
# Description: Assuming that we have some email addresses in the "username@companyname.com" format, please write
#              program to print the user name of a given email address. Both user names and company names are composed
#              of letters only.
# Example:
# If the following email address is given as input to the program:
#
# john@google.com
#
# Then, the output of the program should be: john
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re

email = raw_input('Pls input your email address: ')
pat = "(\w+)@(\w+\.)(com)"
res = re.match(pat, email)
print type(res)
print res.group(1)

