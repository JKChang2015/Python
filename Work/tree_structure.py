# tree_structure
# Created by JKChang
# 11/07/2018, 11:07
# Tag:
# Description: load term & mapping to the ontology to find sub and super
#               find the most common parents

# results/species_url.csv

import pandas as pd
from owlready2 import *
from Work.ontology.onto_info import *

onto_path = '/Users/jkchang/Github/Python/large file/ncbitaxon.owl'

print('loading ontology ... ')
onto = get_ontology(onto_path).load()
print('finish loading... ')

df = pd.read_csv('./results/species_tax_url.csv')
df['sups'] = df['url'].apply(lambda x: information(onto).get_supers(x))
# df['sups_count'] = df['url'].apply(lambda x: information(onto).super_count())
df['subs'] = df['url'].apply(lambda x: information(onto).get_subs(x))
# df['subs_count'] = df['url'].apply(lambda x: information(onto).sub_count())
df.to_csv('./test/species supers and subs.csv', index=False)
