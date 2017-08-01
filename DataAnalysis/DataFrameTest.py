# DataFrameTest
# Created by JKChang
# 31/07/2017, 17:46
# Tag:
# Description: DataFrame testing

from pandas import DataFrame

df = DataFrame({'age': [13, 43, 34],
                'name': ['David', 'Mike', 'Amy']
                })

def2 = DataFrame({'age': [13, 43, 34],
                       'name': ['David', 'Mike', 'Amy']
                       },
                 index=['1st', '2nd', '3rd']
                 )

print(df['age'])
# print df[['age','name']]
print(df.loc['first'])

print('')
