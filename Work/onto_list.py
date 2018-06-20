# onto_list
# Created by JKChang
# 15/06/2018, 11:20
# Tag:
# Description: clean and analysis the sample list

import os

import pandas as pd

#  --- Load the file ---
df = pd.read_csv('all_samples.tsv', sep='\t')
print(df.info())

# split the whole spreadsheet to each samples
indexes = df['Number'].unique()

for i in indexes:
    temp = df.loc[df['Number'] == i]
    temp.drop(temp.index[0], inplace=True)
    temp.to_csv('./split/' + i + '.tsv', index=False, sep='\t')

# --- merge file one by one according to the temple columns

paths = []
for path, subdirs, files in os.walk(os.getcwd() + '/split'):
    for name in files:
        paths.append(os.path.join(path, name))
try:
    paths.remove('/Users/jkchang/Github/Metabolights/JKChang/split/.DS_Store')
except:
    pass

l = ['Number',
     ' "Source Name"',
     'Characteristics[Organism]',
     'Term Source REF[Organism]',
     'Term Accession Number[Organism]',
     'Characteristics[Organism part]',
     'Term Source REF[Organism part]',
     'Term Accession Number[Organism part]']
res = pd.DataFrame(columns=l)  # temple columns

for file in paths:
    temp = pd.read_csv(file, sep='\t')
    print(file)
    res = res.merge(temp, how='outer')

res.to_csv('merged tidied up.tsv', sep='\t')

# --- remove the duplicated row according to the certain columns
res.drop_duplicates(
    subset=[
        'Characteristics[Organism]', 'Term Source REF[Organism]',
        'Term Accession Number[Organism]', 'Characteristics[Organism part]',
        'Term Source REF[Organism part]',
        'Term Accession Number[Organism part]'
    ],
    keep='first',
    inplace=True,
)
res.to_csv('remove duplicated.tsv', sep='\t')
