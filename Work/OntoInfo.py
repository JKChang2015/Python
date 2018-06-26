# test
# Created by JKChang
# 26/06/2018, 11:02
# Tag:
# Description: count amount of subclasses / superclasses


class info(object):
    supers = []
    subs = []

    def __init__(self, onto):
        self.onto = onto

    def __setClass(self, onto_class):
        try:
            self.onto_class = self.onto.search_one(label=onto_class)
        except:
            print('can not find xxx')

    def __get_supers(self, onto_class):
        self.__setClass(onto_class)

        if self.onto_class.label == '':
            return

        for parent in self.onto_class.is_a:
            self.__get_supers(parent)
            self.supers.append(parent.label)

    def __get_subs(self, onto_class):

        if self.onto_class.label == '':
            return

        for child in self.onto_class.subclasses():
            self.__get_subs(child)
            self.subs.append(child.label)

    def SUPERS(self, onto_class):
        self.__get_supers(onto_class)
        self.supers = [list(x)[0] for x in self.supers if len(x) > 0]
        return self.supers

    def SUBS(self, onto_class):
        self.__get_subs(onto_class)
        self.subs = [list(x)[0] for x in self.subs if len(x) > 0]
        return self.subs

    def countSub(self, onto_class):
        self.__get_subs(onto_class)
        return (len(self.subs))

    def countSup(self, onto_class):
        self.__get_supers(onto_class)
        return (len(self.supers))
