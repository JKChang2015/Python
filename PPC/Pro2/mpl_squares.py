# mpl_squares
# Created by JKChang
# 22/01/2018, 13:25
# Tag:
# Description: 

import matplotlib.pyplot as plt

input_Value = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
plt.plot(input_Value, square, linewidth=5)
plt.title('square Nums', fontsize=24)

plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
