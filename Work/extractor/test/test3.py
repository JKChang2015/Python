# test3
# Created by JKChang
# 2019-03-15, 11:44
# Tag:
# Description: 

import pandas as pd
from Work.extractor.fileReader import investigation_reader
from Work.extractor.studyList import getStudyIDs

result = []
studyIDs = ['MTBLS1','MTBLS53','MTBLS54']

for studyID in studyIDs:
    target_flag = investigation_reader(studyID, 'Study Design Type')
    res = [x for x in  target_flag if 'target' in x.lower()]
    target = [x for x in  target_flag if x.lower().startswith('targeted')]
    untarget = [x for x in  target_flag if x.lower().startswith(('untargeted','non-targeted'))]
    if len(target) >0 or len(untarget) > 0:
        res = {'ID':studyID,'Target':len(target), 'Untarget':len(untarget)}
        result.append(res)

print()