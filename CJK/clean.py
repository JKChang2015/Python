# clean
# Created by JKChang
# 24/08/2017, 15:37
# Tag:
# Description: 

# load the text file
# clean the file


def question(path):
    with open(path) as f:
        content = f.readlines()
        res = []
        for line in content:
            line = line.replace('Go to the editor', '')
            line = line.replace('Click me to see the solution', '')
            if len(line) == 0 or line == '\n':
                continue
            res.append(line)

        for index, elem in enumerate(res):

            if not elem[0].isdigit():
                res[index - 1:index] = [''.join(res[index - 1:index + 1])]
                res.remove(index)

        print('\n'.join(res))


path = '/Users/jkchang/Downloads/re.txt'
question(path)


#     with open(path) as f:
#         for line in f:
#             res = ''
#             if line[0].isdigit() and line != '\n':
#                 res += line
#             res = res.replace('Go to the editor', '')
#             res = res.replace('Click me to see the solution', '')
#             print('-' * 30)
#             print(res)
#
#
#
#
# path = '/Users/jkchang/Downloads/xxx.txt'
# with open(path) as f:
#     for line in f:
#         nextline = next(f)
#         print(line)


# with io.open('/Users/jkchang/Downloads/ree.txt', 'w', encoding="utf-8") as f:
#     f.write(res)
