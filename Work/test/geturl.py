# geturl
# Created by JKChang
# 10/07/2018, 11:58
# Tag:
# Description: get iri from entity label

from owlready2 import *
import pandas as pd
from Work.ontology_info import *


onto = get_ontology('file://./test/infor.owl').load()
df = pd.read_csv('./test/tst.csv')
df['iris'] = df['entity'].apply(lambda x: information(onto).get_iri(x))



# for ele in df.entity:
#     i = information(onto)
#     print(i.get_iri(ele))

df.to_csv('./test/url.csv')