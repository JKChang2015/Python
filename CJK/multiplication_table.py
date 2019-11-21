# multiplication_table
# Created by JKChang
# 18/11/2019, 13:07
# Tag:
# Description: 

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} x {i} = ' + str(i * j), end='\t')
    print()


print('\n'.join('\t'.join([f'{j} x {i} = ' + str(j * i) for j in range(1, i + 1)]) for i in range(1, 10)))
