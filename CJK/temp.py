# temp
# Created by JKChang
# 19/03/2018, 11:08
# Tag:
# Description: 



# for x in range(9,101):
#     num = "{0:0=3d}".format(x)
#     print('{ \n'
#           '\t "cell_type": "code",\n'
#           '\t "execution_count": null,\n'
#           '\t "metadata": {}, \n'
#           '\t "outputs": [], \n'
#           '\t "source": [ \n '
#           '\t\t "# ' + num + '" \n'
#           '\t ]\n'
#          '},'
#
#     )
#

s = input('please input sequence of text:')
d = {}
for char in s:
    if char.isdigit():
        d['DIGITS'] += 1
    elif char.isalpha():
        d['LETTERS'] += 1
    else:
        pass
print(d)
