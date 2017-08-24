# clean
# Created by JKChang
# 24/08/2017, 15:37
# Tag:
# Description: 

# load the text file
# clean the file

path = '/Users/jkchang/Downloads/re.txt'
res = ''
with open(path) as f:
    for line in f:
        test = next(f)
        line = line.replace('Go to the editor', '')
        line = line.replace('Click me to see the solution', '')
        if line != '\n':
            res += line

print(res)


