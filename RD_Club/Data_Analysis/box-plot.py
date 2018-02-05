# box-plot
# Created by JKChang
# 23/01/2018, 11:30
# Tag:
# Description: bot-plot analysis

import matplotlib.pyplot as plt
import pandas
import seaborn as sns



data = pandas.read_csv(r'./resources/HR_comma_sep.csv')
data = data.rename(columns={'sales': 'Departments'})

print(data.info())

columns_name = list(data.columns.values)
columns_name.remove('left')

plt.figure()
plt.tight_layout()



for col in columns_name:
    sns.boxplot(x='left', y=col, data=data)
    plt.savefig('results/' + col + ' box-plot.png', bbox_inches='tight')
    plt.show()

