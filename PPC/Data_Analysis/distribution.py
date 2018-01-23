# distribution
# Created by JKChang
# 23/01/2018, 09:16
# Tag:
# Description: elements distribution

import matplotlib.pyplot as plt
import pandas
import seaborn as sns

data = pandas.read_csv(r'./resources/HR_comma_sep.csv')
data = data.rename(columns={'sales': 'Departments'})

columns_name = list(data.columns.values)
columns_name = [x for x in columns_name if
                x not in ['left', 'satisfaction_level', 'last_evaluation', 'average_montly_hours']]


for col in columns_name:
    plt.figure()
    sns.countplot(x='left', data=data, hue=col)
    plt.ylabel(col, fontsize=14)
    plt.savefig('results/'+col + '.png', bbox_inches='tight')
    plt.show()

# Set scatter data into groups
excepts = ['satisfaction_level', 'last_evaluation', 'average_montly_hours']

for group in excepts:
    labels = []
    if group == 'satisfaction_level':
        labels = ['very unsatisfied', 'unsatisfied', 'satisfied', 'very satisfied']
    elif group == 'last_evaluation':
        labels = ['low', 'medium', 'high', 'very high']
    elif group == 'average_montly_hours':
        labels = ['short', 'usual', 'long', 'crazy']

    bins = [min(data.satisfaction_level), 0.5 * data.satisfaction_level.mean(), data.satisfaction_level.mean(),
            1.5 * data.satisfaction_level.mean(), max(data.satisfaction_level)]

    data[group + ' '] = pandas.cut(data.satisfaction_level, bins, right=True, labels=labels)

    sns.countplot(x='left', data=data, hue=group + ' ')
    plt.ylabel(group, fontsize=14)
    plt.savefig('results/'+group + '.png', bbox_inches='tight')
    plt.show()
