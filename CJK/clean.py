# clean
# Created by JKChang
# 24/08/2017, 15:37
# Tag:
# Description: 

# load the text file
# clean the file

import string


def question(path):
    with open(path) as f:

        content = f.read()
        s = content
        lines = content.split('\n')
        serial = []
        for line in lines:
            translator = str.maketrans('', '', string.punctuation)
            line = line.translate(translator)
            if len(line) != 0 and line != '\n':
                value = line.split()[0]
                if value.isdigit():
                    serial.append(value)
        print(serial)

        res = []
        for ser in serial[1:]:
            res.append(s.split(ser, 1)[0])
            s = ser + s.split(ser, 1)[1]
        res.append(s)
        print('>'.join(res))
        return res



        # res = []
        #
        # for line in content:
        #     line = line.replace('Go to the editor', '')
        #     line = line.replace('Click me to see the solution', '')
        #     if len(line) == 0 or line == '\n':
        #         continue
        #     res.append(line)
        #


path = '/Users/jkchang/Downloads/ree.txt'
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
