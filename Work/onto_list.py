# onto_list
# Created by JKChang
# 15/06/2018, 11:20
# Tag:
# Description: clean and analysis the sample list

import pandas as pd

df = pd.read_csv('result.tsv', sep='\t')

#  merge two entity name / url columns

data1 = df[['Number', 'Characteristics[Organism]', 'Term Accession Number[Organism]']]
data1 = data1.rename(index=str, columns={'Number': 'Index', 'Characteristics[Organism]': "Entities",
                                         'Term Accession Number[Organism]': "Url"})

data2 = df[['Number', 'Characteristics[Organism part]', 'Term Accession Number[Organism part]']]
data2 = data2.rename(index=str, columns={'Number': 'Index', 'Characteristics[Organism part]': "Entities",
                                         'Term Accession Number[Organism part]': "Url"})

res = [data1, data2]
data = pd.concat(res)

# drop NaN
data.dropna(inplace=True)
# drop duplicated according to two columns
data.drop_duplicates(subset=['Entities', 'Url'], keep='first', inplace=True)

data = data.sort_values(by='Entities')

data.to_csv('cleaned.tsv', index=False, sep='\t')

data.info()
