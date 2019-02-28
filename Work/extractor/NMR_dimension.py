# NMR_dimension
# Created by JKChang
# 2019-02-27, 20:43
# Tag:
# Description: extract dimension information from Assay files

import pandas as pd

from Work.extractor.fileReader import assay_reader
from Work.extractor.fileReader import investigation_reader

df = pd.read_csv('../resources/MTBLS Curation Status Log.csv')
df = df.dropna(subset=['StudySize'])
studyIDs = df[df['Technique'].str.contains('NMR', na=False)]['ACC'].tolist()
print()

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
res_df = pd.DataFrame(columns=['StudyID', 'Technique'])

for studyID in studyIDs:
    print(studyID)

    studyPath = folderPath + studyID + '/'
    assayList = investigation_reader(studyID, 'Study Assay File Name')
    assayList = list(set(assayList))

    if len(assayList) == 0:
        continue

    dimensions = []
    for assay in assayList:
        # print('read', studyPath + assay)
        try:

            dimensions += assay_reader(studyPath + assay, 'Parameter Value[Pulse sequence name]')
            dimensions = list(set(dimensions))
        except Exception as e:
            print(e.args)
            pass

    if len(dimensions) == 0:
        continue

    for dimension in dimensions:
        res_df = res_df.append({'StudyID': studyID, 'Technique': dimension}, ignore_index=True)

res_df.to_csv('dimensions.tsv', sep='\t', index=False)
