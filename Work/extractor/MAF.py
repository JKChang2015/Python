# BBSRC
# Created by JKChang
# 2019-02-15, 10:48
# Tag:
# Description:

from Work.extractor.fileReader import *
from Work.extractor.studyList import *


class MAFstatus():
    def __init__(self, studyID, fullsize, annotated, unknown):
        self.studyID = studyID
        self.fullsize = fullsize
        self.annotated = annotated
        self.unknown = unknown


studyIDs = getStudyIDs(publicStudy=True)

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
res = []
unknown_terms = []

for studyID in studyIDs:
    print(studyID)

    studyPath = folderPath + studyID + '/'
    assayList = investigation_reader(studyID, 'Study Assay File Name')
    assayList = list(set(assayList))

    study_full, study_annotated, study_unknown = 0, 0, 0

    if len(assayList) == 0:
        continue

    mafList = []
    for assay in assayList:
        mafList += assay_reader(studyPath + assay, 'Metabolite Assignment File')
        mafList = list(set(mafList))

    if len(mafList) == 0:
        continue

    for maf in mafList:
        try:
            df = pd.read_csv(studyPath + maf, sep='\t')
            annotated = df.loc[(df['database_identifier'].notnull()) | (df['metabolite_identification'].notnull())]
            unknown = annotated.loc[~annotated['database_identifier'].astype(str).str.startswith(
                ('CHEBI', 'HMDB', 'CSID', 'TG', 'DG', 'P', 'L', 'C', 'SM', 'PubChem'), na=True)]

            term = list(unknown['database_identifier'].unique())
            unknown_terms = unknown_terms + list(set(term) - set(unknown_terms))
            study_full += df.shape[0]
            study_annotated += (annotated.shape[0] - unknown.shape[0])
            study_unknown += unknown.shape[0]
        except:
            print(studyID, maf)
            continue

    status = MAFstatus(studyID, fullsize=study_full, annotated=study_annotated, unknown=study_unknown)
    res.append(status)

df = pd.DataFrame(columns=['studyID', 'annotated', 'unknown', 'un-annotated'])
for maf in res:
    unannotated = maf.fullsize - maf.annotated - maf.unknown
    temp = pd.Series([maf.studyID, maf.annotated, maf.unknown, unannotated], index=df.columns)
    df = df.append(temp, ignore_index=True)

df.to_csv('maff_results.tsv', sep='\t', index=False)
