# t
# Created by JKChang
# 26/06/2018, 14:47
# Tag:
# Description: 

from Work.testing import *
from owlready2 import *

onto = get_ontology('file://./infor.owl').load()
f = information(onto)
print(f.get_supers('pink lady'))
print(f.super_count('pink lay'))
print(f.get_subs('pink lady'))
print(f.sub_count('pink lay'))