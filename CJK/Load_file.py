import os

file =  '/resources/test.txt'
path = os.getcwd()+file
# Same with: path = '/Users/jkchang/Github/Python/CJK' +file
result = open(path, 'r+')

print result.read()

