# sample_data_cleaning
# Created by JKChang
# 20/06/2018, 09:59
# Tag:
# Description: Clean and analysis the sample list

import pandas as pd

df = pd.read_csv('./resources/all_samples.tsv', sep='\t')
print(df.info())

# templet of the result file
head = ['Number',
        ' "Source Name"',
        'Characteristics[Organism]',
        'Term Source REF[Organism]',
        'Term Accession Number[Organism]',
        'Characteristics[Organism part]',
        'Term Source REF[Organism part]',
        'Term Accession Number[Organism part]']
res = pd.DataFrame(columns=head)

indexes = df['Number'].unique()
for i in indexes:
    # split the file according to the Study ID
    study = df.loc[df['Number'] == i]

    # keep the original header (2nd row)
    new_header = study.iloc[0]
    study = study[1:]
    study.columns = new_header
    study.columns.values[0] = 'Number'

    # clean useful columns
    templet_head = ['Number',
                    ' "Source Name"',
                    'Characteristics[Organism]',
                    'Term Source REF',
                    'Term Accession Number',
                    'Characteristics[Organism part]',
                    'Term Source REF.1',
                    'Term Accession Number.1'
                    ]
    study = study.loc[:, study.columns.isin(templet_head)]

    # rename the duplicated columns
    dic = {
        'Term Source REF': ['Term Source REF[Organism]', 'Term Source REF[Organism part]'],
        'Term Accession Number': ['Term Accession Number[Organism]', 'Term Accession Number[Organism part]']
    }

    study = study.rename(columns=lambda c: dic[c].pop(0) if c in dic.keys() else c)

    # merge to one
    res = res.merge(study, how='outer')

    # drop duplicated
    res.drop_duplicates(
        subset=[
            'Term Accession Number[Organism]',
            'Term Accession Number[Organism part]'
        ],
        keep='first',
        inplace=True, )

    # drop numerical only rows
    res['Characteristics[Organism]'].fillna(' ', inplace=True)
    t = res['Characteristics[Organism]'].str.isdigit()
    res = res[~t]

res.to_csv('result.tsv', index=False, sep='\t')
