# map_EFO
# Created by JKChang
# 24/07/2018, 16:50
# Tag:
# Description:

import pandas as pd
from owlready2 import *

from Work.ontology_info import *
#
onto = get_ontology('./efo.owl').load()
# df = pd.read_csv('./efo.csv')
# df['supers'] = df['Entities'].apply(lambda x: information(onto).get_supers(x))
# df.to_csv('./efo_supers.csv')

root = 'process'
