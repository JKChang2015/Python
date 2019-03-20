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

from Work.extractor.fileReader import investigation_reader
from Work.extractor.studyList import getStudyIDs

studyIDs = getStudyIDs(publicStudy=True)
print()

