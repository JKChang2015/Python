# confidence
# Created by JKChang
# 2019-02-13, 18:17
# Tag:
# Description: extract confidence from MAF file

import pandas as pd

from Work.extractor.MAF_reader import assay_reader
from Work.extractor.MAF_reader import investigation_reader
from Work.extractor.studyList import getStudyIDs


class confidence():
    def __init__(self, studyID, zero=0, oneStar=0, twoStar=0, threeStar=0, fourStar=0, fiveStar=0):
        self.studyID = studyID
        self.zero = zero
        self.oneStar = oneStar
        self.twoStar = twoStar
        self.threeStar = threeStar
        self.fourStar = fourStar
        self.fiveStar = fiveStar


folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
studyIDs = getStudyIDs(publicStudy=True)
res = {}
study_count = 0

key = []

for studyID in studyIDs:
    # print(studyID)
    studyPath = folderPath + studyID + '/'
    oneStar, twoStar, threeStar, fourStar, fiveStar = 0, 0, 0, 0, 0

    try:
        assayList = investigation_reader(studyID, 'Study Assay File Name')
        mafList = []

        for assay in assayList:
            mafList += assay_reader(studyPath + assay, 'Metabolite Assignment File')
            mafList = list(set(mafList))

        if len(mafList) > 0:
            for maf_file in mafList:
                try:
                    df = pd.read_csv(studyPath + maf_file, sep='\t')
                    count = df['reliability'].value_counts().to_dict()
                    res[studyID] = count
                    key += list(set(count.keys()))
                    if len(count) > 0:
                        study_count += 1
                        print(studyID+';' ,  count)
                except:
                    print('Fail to read maf file:', maf_file)
    except:
        print('fail to read investigation file of ', studyID)
        pass

# r = sorted(list(set([str(x).lower().strip() for x in key])))
# print(study_count)
# print('\n'.join(r))
