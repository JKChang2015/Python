# NMR_dimension
# Created by JKChang
# 2019-02-27, 20:43
# Tag:
# Description: extract dimension information from Assay files

import pandas as pd

from Work.extractor.fileReader import assay_reader
from Work.extractor.fileReader import investigation_reader

tech = 'NMR'

df = pd.read_csv('./splited.tsv',sep='\t')

# for public/ in review only
df = df[df['Classify']== tech]
studyIDs = list(set(df['MTBLS ID'].tolist()))

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

#
#
#
# # df = pd.read_csv('../resources/MTBLS Curation Status Log.tsv',sep= '\t')
# # df = df[df['Status'].isin (['Public','In Review' ])]
# df = pd.read_csv('./splited.tsv',sep= '\t')
#
# NMR_studies = df[df['Study Type'].isin(['NMR','MAS-NMR'])]['MTBLS ID'].tolist()
#
# print(len(set(NMR_studies)))
#
# folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
# res_df = pd.DataFrame(columns=['StudyID', 'Technique'])
#
# for studyID in NMR_studies:
#     print(studyID)
#
#     studyPath = folderPath + studyID + '/'
#     assayList = investigation_reader(studyID, 'Study Assay File Name')
#     assayList = list(set(assayList))
#
#     if len(assayList) == 0:
#         continue
#
#     dimensions = []
#     for assay in assayList:
#         # print('read', studyPath + assay)
#         try:
#
#             dimensions += assay_reader(studyPath + assay, 'Parameter Value[Pulse sequence name]')
#             dimensions = list(set(dimensions))
#         except Exception as e:
#             print(e.args)
#             pass
#
#     if len(dimensions) == 0:
#         continue
#
#     for dimension in dimensions:
#         res_df = res_df.append({'StudyID': studyID, 'Technique': dimension}, ignore_index=True)


