# mapping_species
# Created by JKChang
# 10/07/2018, 12:08
# Tag:
# Description: mapping study species to different ontologies

import pandas as pd
from owlready2 import *

from Work.ontology_info import *

# load ontologies:
onto_list = ['bto', 'efo', 'ncbitaxon']  # 'bto', 'efo'
onto_path = '/Users/jkchang/Github/Python/large file'


for onto_name in onto_list:
    print('loading %s' % onto_name)
    onto = get_ontology(os.path.join(onto_path, onto_name) + '.owl').load()
    print('finish loading...')
    df = pd.read_csv(r'./results/url.csv')
    df[onto_name] = df['species'].apply(lambda x: information(onto).get_iri(x))
    df.to_csv('./results/url.csv', index=False)
