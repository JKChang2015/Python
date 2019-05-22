import types

from owlready2 import get_ontology


def addEntity(ontoPath, new_term, supclass, definition=None):
    try:
        onto = get_ontology(ontoPath).load()
        id = getid(onto)
        namespace = onto.get_namespace('http://www.ebi.ac.uk/metabolights/ontology/')

        with namespace:
            try:
                cls = onto.search_one(label=supclass)
            except:
                try:
                    cls = onto.search_one(iri=supclass)
                except Exception as e:
                    print(e)

            newEntity = types.new_class(id, (cls,))
            newEntity.label = new_term
            if definition != None:
                newEntity.isDefinedBy = definition
            else:
                pass

        onto.save(file=ontoPath, format='rdfxml')

    except Exception as e:
        print(e)


def getid(onto):
    temp = []
    for c in onto.classes():
        if str(c).startswith('metabolights'):
            temp.append(str(c))

    last = max(temp)
    temp = str(int(last[-6:]) + 1).zfill(6)
    id = 'MTBLS_' + temp

    return id


# addEntity('./resources/metabolights.owl', 'papapa', 'role', 'papap def')
