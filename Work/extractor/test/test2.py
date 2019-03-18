# test2
# Created by JKChang
# 2019-03-14, 10:47
# Tag:
# Description: 

import pandas as pd
from Work.extractor.fileReader import investigation_reader
from Work.extractor.studyList import getStudyIDs


# tech = 'LC-MS'
# df = pd.read_csv('../res/splited.tsv',sep='\t')
# df = df[df['Classify']== tech]
# studyIDs = sorted(list(set(df['MTBLS ID'].tolist())))

studyIDs = getStudyIDs(publicStudy=True)

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'

count = 0
result = []

for studyID in studyIDs:
    print(studyID)

    studyPath = folderPath + studyID + '/'
    target_flag = investigation_reader(studyID, 'Study Design Type')
    res = [x for x in  target_flag if 'target' in x.lower()]
    target = [x for x in  target_flag if x.lower().startswith('targeted')]
    untarget = [x for x in  target_flag if x.lower().startswith(('untargeted','non-targeted'))]
    if len(target) >0 or len(untarget) > 0:
        count +=  1
    res = {'ID':studyID,'Target':len(target), 'Untarget':len(untarget)}
    result.append(res)

print(count)
res_df = pd.DataFrame(result)

res_df.to_csv('../res/'+"ALL"+' target.tsv',sep ='\t',index=False)

print()