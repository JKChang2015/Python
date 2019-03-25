# onto_validation
# Created by JKChang
# 2019-03-18, 09:45
# Tag:
# Description: validation of ontology terms (factors)

'''
Steps:
1. get list of public/ In_review studyIDs\
2. extract factor, mapped term, mapped iri from the investigation file

3. validation terms:
    3.1 compare term with mapped term, if equals record as done
    3.2 else mapping term with OLS exact match, got mapped term and iri, marked as correction
    3.3 else doing fuzzy matches with OLS search, marked as suggestion
    3.4 else rest of terms need to further discussion

'''

# =============================================================================
#                               STE 1 -2
# =============================================================================

# from Work.extractor.fileReader import investigation_reader
# from Work.extractor.studyList import getStudyIDs
#
# import pandas as pd
#
# studyIDs = getStudyIDs(publicStudy=True)
#
#
# count = 0
# res =[]
# for studyID in studyIDs:
#     print(studyID)
#     pair = investigation_reader(studyID,prefix=['Study Factor Name','Study Factor Type','Study Factor Type Term Accession Number'])
#     res += pair
#
#
# df = pd.DataFrame(res)
# df = df[['StudyID','Study Factor Name','Study Factor Type','Study Factor Type Term Accession Number']]
# df.to_csv('factors.tsv', sep='\t', index=False)

# =============================================================================
#                               STEP 2
# =============================================================================

# 1. Data cleaning

import pandas as pd
#
df = pd.read_csv('factors.tsv', sep='\t')
df = df.dropna(subset=['Study Factor Name'])
df = df.reset_index(drop=True)
# res = df[df[['Study Factor Type','Study Factor Type Term Accession Number']].isnull().any(axis=1)]

# 2. check if exact correct
def OLS_validation(iri):
    from urllib.parse import quote_plus
    from owlready2 import urllib
    import json

    try:
        print(iri)
        ir = quote_plus(quote_plus(iri))
        url = 'http://www.ebi.ac.uk/ols/api/terms/findByIdAndIsDefiningOntology/' + ir
        fp = urllib.request.urlopen(url)
        content = fp.read().decode('utf-8')
        j_content = json.loads(content)

        label = j_content['_embedded']['terms'][0]['label']
        return label


    except:
        return ''

df['IRI_label'] = df['Study Factor Type Term Accession Number'].apply(OLS_validation)

# 3. Check

# df = pd.read_csv('label.tsv',sep='\t')
correct = df[(df['Study Factor Name'].str.lower() == df['IRI_label'].str.lower()) &  (df['IRI_label'].str.lower() == df['Study Factor Type'].str.lower())]
# cor_index = correct.index
incorrect = df.drop(index=correct.index)
correct.to_csv('correct.tsv', sep='\t', index=False)
incorrect.to_csv('incorrect.tsv', sep='\t', index=False)



