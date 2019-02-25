# ontology_ws
# Created by JKChang
# 2019-02-21, 10:48
# Tag:
# Description: rewrite ontology-ws

from owlready2 import IRIS
from owlready2 import get_ontology

from Work.ontology.ontology_info import entity
from Work.ontology.ontology_info import onto_information


def getMetaboTerm(keyword, branch):
    # logger.info('Getting Ontology term %s', keyword)
    onto = get_ontology('../resources/Metabolights.owl').load()
    info = onto_information(onto)

    res_cls = []
    result = []
    if keyword:
        if branch:  # term = 1, branch = 1, search term in the branch
            try:
                start_cls = onto.search_one(label=branch)
                clses = info.get_subs(start_cls)
            except Exception as e:
                print(e.args)
                return []
        else:  # term = 1, branch = 0, search term in the whole ontology
            try:
                clses = list(onto.classes())
            except Exception as e:
                print(e.args)
                return []

        #  exact match
        for cls in clses:
            if keyword.lower() == cls.label[0].lower():
                subs = info.get_subs(cls)
                res_cls = [cls] + subs

        # if not exact match, do fuzzy match
        if len(res_cls) == 0:
            for cls in clses:
                if cls.label[0].lower().startswith(keyword.lower()):
                    res_cls.append(cls)
                    res_cls += info.get_subs(cls)

        # synonym match
        if branch == 'taxonomy' or branch == 'factors':
            for cls in clses:
                try:
                    map = IRIS['http://www.geneontology.org/formats/oboInOwl#hasExactSynonym']
                    Synonym = list(map[cls])
                    if keyword.lower() in [syn.lower() for syn in Synonym]:
                        res_cls.append(cls)
                except Exception as e:
                    print(e.args)
                    pass

    elif keyword is None and branch:  # term = 0, branch = 1, return whole branch
        try:
            start_cls = onto.search_one(label=branch)
        except Exception as e:
            print(e.args)
            return []
        res_cls = info.get_subs(start_cls)

    else:  # term = 0, branch = 0, return []
        return []

    if len(res_cls) > 0:
        for cls in res_cls:
            if 'MTBLS' in cls.iri:
                ontoName = 'MTBLS'
            else:
                ontoName = getOnto_Name(cls.iri)

            enti = entity(name=cls.label[0], iri=cls.iri, obo_ID=cls.name, ontoName=ontoName,
                          provenance_name='Metabolights', provenance_uri='https://www.ebi.ac.uk/metabolights/')
            result.append(enti)
        return result
    return []


def getOnto_Name(iri):
    # get ontology name by giving iri of entity
    substring = iri.rsplit('/', 1)[-1]
    return ''.join(x for x in substring if x.isalpha())


keyword = 'cell'
branch = None

res = getMetaboTerm(keyword, branch)
print()
