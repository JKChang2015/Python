# Q059
# Created by JKChang
# 05/05/2017, 09:46
# Tag: regular expression match
# Description: Assuming that we have some email addresses in the "username@companyname.com" format, please write
#              program to print the company name of a given email address. Both user names and company names are
#              composed of letters only.

import re

email = raw_input('Please input your email address: ')
pa = '(\w+)@(\w+)\.(\w+)'
mat = re.match(pa, email)
print 'name is: ', mat.group(1)
print 'company name is: ', mat.group(2)
