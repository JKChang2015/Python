# removeDuplicatedresult
# Created by JKChang
# 07/11/2018, 12:07
# Tag:
# Description: 

from Work.ontology_info import entity


def removeDuplicated(res_list):
    priority = {'MTBLS': 0, 'NCBITAXON': 1, 'BTO': 2, 'EFO': 3, 'CHEBI': 4, 'CHMO': 5, 'NCIT': 6, 'PO': 7}
    res = {}
    for enti in res_list:
        term_name = enti.name.lower()
        onto_name = enti.ontoName
        try:
            prior = priority.get(onto_name)
        except:
            prior = 1000

        if term_name in res:
            try:
                old_prior = priority.get(res[term_name].ontoName)
            except:
                old_prior = 1000

            if prior < old_prior:
                res[term_name] = enti

        else:
            res[term_name] = enti

    return list(res.values())


e1 = entity(name="mass spectrometry", iri="www.google.com", obo_ID="NICT123", ontoName="NCIT",
            provenance_name="Metabolights", provenance_uri="www.ebi.ac.uk", Zooma_confidence="high")

e2 = entity(name="mass spectrometry", iri="www.google.com", obo_ID="NCBITAXON231", ontoName="NCBITAXON",
            provenance_name="Metabolights", provenance_uri="www.ebi.ac.uk", Zooma_confidence="high")

e3 = entity(name="Mass spectrometry", iri="www.google.com", obo_ID="BTO231", ontoName="BTO",
            provenance_name="Metabolights", provenance_uri="www.ebi.ac.uk", Zooma_confidence="high")

e4 = entity(name="mass Spectrometry", iri="www.google.com", obo_ID="CHEBI22", ontoName="CHEBI",
            provenance_name="Metabolights", provenance_uri="www.ebi.ac.uk", Zooma_confidence="high")

res = [e1, e2, e3, e4]
r = removeDuplicated(res)
print(r)
