# temp
# Created by JKChang
# 19/03/2018, 11:08
# Tag:
# Description: 

# {
#     "cell_type": "code",
#     "execution_count": null,
#     "metadata": {},
#     "outputs": [],
#     "source": [
#         "# 009"
#     ]
# },

for x in range(9,101):
    num = "{0:0=3d}".format(x)
    print('{ \n'
          '\t "cell_type": "code",\n'
          '\t "execution_count": null,\n'
          '\t "metadata": {}, \n'
          '\t "outputs": [], \n'
          '\t "source": [ \n '
          '\t\t "# ' + num + '" \n' 
          '\t ]\n'
         '},'

    )

#     "execution_count": null,
#     "metadata": {},
#     "outputs": [],
#     "source": [')
    print( )
