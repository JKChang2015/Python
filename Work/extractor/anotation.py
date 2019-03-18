# anotation
# Created by JKChang
# 2019-03-14, 11:08
# Tag:
# Description:  anotated, know-unknow, unknow-unknow

from Work.extractor.fileReader import investigation_reader,assay_reader
from Work.extractor.studyList import getStudyIDs

import pandas as pd
import numpy as np

class MAFstatus():
    def __init__(self, studyID, fullsize, annotated, unknown):
        self.studyID = studyID
        self.fullsize = fullsize
        self.annotated = annotated
        self.unknown = unknown


studyIDs = getStudyIDs(publicStudy=True)

# tech = "GC-MS"
#
# df = pd.read_csv('./splited.tsv',sep='\t')
#
# # for public/ in review only
# df = df[df['Classify']== tech]
# studyIDs = list(set(df['MTBLS ID'].tolist()))

FolderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'

res = []
count = 0
unknown_terms = []

for studyID in studyIDs:
    count += 1
    print(studyID)
    studyPath = FolderPath + studyID + '/'
    study_full, study_annotated, study_unknown = 0, 0, 0

    try:
        assayList = investigation_reader(studyID, 'Study Assay File Name')
        mafList = []

        for assay in assayList:
            mafList += assay_reader(studyPath + assay, 'Metabolite Assignment File')
            mafList = list(set(mafList))

        try:
            if len(mafList) > 0:
                for maf_file in mafList:
                    try:
                        df = pd.read_csv(studyPath + maf_file, sep='\t')
                        # df = df.astype(str)
                        annotated = df.loc[
                            (df['database_identifier'].notnull()) | (df['metabolite_identification'].notnull())]
                        unknown = annotated.loc[~annotated['database_identifier'].astype(str).str.startswith(
                            ('CHEBI', 'HMDB', 'CSID', 'TG', 'DG', 'P', 'L', 'C', 'SM', 'PubChem'), na=True)]

                        term = list(unknown['database_identifier'].unique())
                        unknown_terms = unknown_terms + list(set(term) - set(unknown_terms))
                        study_full += df.shape[0]
                        study_annotated += (annotated.shape[0] - unknown.shape[0])
                        study_unknown += unknown.shape[0]

                    except:
                        print(studyID, maf_file)
                        continue
        except:
            print('Fail to load MAF file from ', studyID)
            continue

        status = MAFstatus(studyID, fullsize=study_full, annotated=study_annotated, unknown=study_unknown)
        res.append(status)
    except:
        print('Fail to load investigation file from ', studyID)
        continue

# print(unknown_terms)
# cols = ['database_identifier','metabolite_identification']

df = pd.DataFrame(columns=['studyID', 'annotated', 'unknown', 'un-annotated'])
for maf in res:
    # try:
    unannotated = maf.fullsize - maf.annotated - maf.unknown
    # print(unannotated)
    temp = pd.Series([maf.studyID, maf.annotated, maf.unknown, unannotated],
                     index=df.columns)
    df = df.append(temp, ignore_index=True)
    # except:
    #     print('something wrong with' + maf.studyID)
df.replace(0, np.nan)

df.to_csv('ALL annotation.tsv', sep='\t', index=False)


