# test
# Created by JKChang
# 26/06/2018, 11:02
# Tag:
# Description: count amount of subclasses / superclasses

from owlready2 import *


class OntoInfo(object):
    def __init__(self, onto):
        self.onto = onto

    def __setClass(self, onto_class):
        try:
            self.onto_class = self.onto.search_one(label=onto_class)
        except:
            print('can not find xxx')



    def get_supers(self, onto_class):
        supers = []
        if self.onto_class.label == '':
            return

        for parent in onto_class.is_a:
            self.get_supers(parent)
            supers.append(parent.label)
            print('  is a %s' % parent.label)

        return supers

    def get_subs(self, onto_class):
        subs = []
        if self.onto_class.label == '':
            return

        return subs

    def countSub(self, onto_class):
        self.__setClass(onto_class)
        return len(self.get_supers(self.onto_class))

    def countSup(self, onto_class):
        self.__setClass(onto_class)
        return len(self.get_supers(self.onto_class))


onto = get_ontology('file://./infor.owl').load()

onto_info = OntoInfo(onto)
