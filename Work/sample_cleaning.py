# sample_cleaning
# Created by JKChang
# 09/07/2018, 11:20
# Tag:
# Description: extract information from the all_sample file

import pandas as pd

# read the all_sample file
df = pd.read_csv('./resources/all_samples.tsv', sep='\t')
print(df.info())

study_ID = df['Number'].unique()

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

for i in study_ID:
    # split the sample file according to the Study ID
    study = df.loc[df['Number'] == i]

    # Keep the original header
    new_header = study.iloc[0]
    study = study[1:]
    study.columns = new_header

    # rename the df[0][0]
    study.columns.values[0] = 'Number'

    # extract useful columns
    sample_head = ['Number', ' "Source Name"', 'Characteristics[Organism]',
                   'Term Source REF', 'Term Accession Number',
                   'Characteristics[Organism part]', 'Term Source REF.1',
                   'Term Accession Number.1'
                   ]
    study = study.loc[:, study.columns.isin(sample_head)]

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

res.to_csv('./results/cleaned data.tsv', index=False, sep='\t')

