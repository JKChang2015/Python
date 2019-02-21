# ontology_ws
# Created by JKChang
# 2019-02-21, 10:48
# Tag:
# Description: rewrite ontology-ws

import datetime
import json
import logging
import ssl

import numpy as np
import pandas as pd
from flask import jsonify
from flask import request, abort, current_app as app
from flask_restful import Resource, reqparse
from flask_restful_swagger import swagger
from owlready2 import get_ontology, urllib, IRIS


class entity():
    def __init__(self, name=None, iri=None, obo_ID=None, ontoName=None, provenance_name=None, provenance_uri=None,
                 Zooma_confidence=None):
        if name is None:
            self.name = ''
        else:
            self.name = name

        if iri is None:
            self.iri = ''
        else:
            self.iri = iri

        if obo_ID is None:
            self.obo_ID = ''
        else:
            self.obo_ID = obo_ID

        if ontoName is None:
            self.ontoName = ''
        else:
            self.ontoName = ontoName

        if provenance_name is None:
            self.provenance_name = ''
        else:
            self.provenance_name = provenance_name

        if provenance_uri is None:
            self.provenance_uri = ''
        else:
            self.provenance_uri = provenance_uri

        if Zooma_confidence is None:
            self.Zooma_confidence = ''
        else:
            self.Zooma_confidence = Zooma_confidence


class ontology():

    def get_subclass(self):
        pass

    def get_superclass(self):
        pass

    def get_zooma(self):
        pass

    def get_OLS(self):
        pass

    def get_bioportal(self):
        res = []
        try:
            url = 'http://data.bioontology.org/search?q=' + keyword.replace(' ', "+")  # + '&require_exact_match=true'
            request = urllib.request.Request(url)
            request.add_header('Authorization', 'apikey token=c60c5add-63c6-4485-8736-3f495146aee3')
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            j_content = json.loads(content)

            iri_record = []

            for term in j_content['collection']:
                iri = term['@id']
                if iri in iri_record:
                    continue

                if 'mesh' in iri.lower():
                    ontoName = 'MESH'
                elif 'nci' in iri.lower():
                    ontoName = 'NCIT'
                elif 'bao' in iri.lower():
                    ontoName = 'BAO'
                else:
                    ontoName = __get_onto_name__(iri)

                enti = entity(name=term['prefLabel'],
                              iri=iri,
                              obo_ID=iri.rsplit('/', 1)[-1],
                              ontoName=ontoName)
                res.append(enti)
                iri_record.append(iri)
                if len(res) >= 5:
                    break
        except Exception as e:
            # TODO
            print('getBioportal' + str(e))
            # logger.error('getBioportal' + str(e))
        return res


def __get_onto_name__(iri):
    # get ontology name by giving iri of entity
    substring = iri.rsplit('/', 1)[-1]
    return ''.join(x for x in substring if x.isalpha())



term = False
branch = False
exact = False

if term == True:
    if branch == True:  # term == True branch == True
        pass
    else:  # term == True branch == False
        pass

else:
    if branch == True:  # term == False branch == True
        pass
    else:  # term == False branch == False
        pass
