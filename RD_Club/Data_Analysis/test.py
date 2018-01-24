# test
# Created by JKChang
# 23/01/2018, 10:04
# Tag:
# Description: 

import pandas as pd

a = [1,3,5,7,1,2]

print(pd.qcut(a, 3, labels=["good", "medium", "bad"]))


