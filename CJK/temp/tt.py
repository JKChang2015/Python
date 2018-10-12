# tt
# Created by JKChang
# 11/10/2018, 15:29
# Tag:
# Description: 

keyword = 'lung'
url = 'https://www.ebi.ac.uk/ols/api/search?q=' + keyword.replace(' ', "+") + \
              '&groupField=true' \
              '&queryFields=label,synonym' \
              '&fieldList=iri,label,short_form,obo_id,ontology_name,ontology_prefix'

print(url)