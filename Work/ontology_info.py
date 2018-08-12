# testing
# Created by JKChang
# 26/06/2018, 14:09
# Tag:
# Description: 

class information():
    ''' basic information of entities'''

    def __init__(self, onto):
        '''initialization'''
        self.onto = onto

    def get_subs(self, txt):

        '''return list of sub classes'''

        print('matching subs of %s' % txt)
        sub = []
        try:
            onto_c = self.onto.search_one(label=txt)
            if (len(onto_c) == 0):
                onto_c = self.onto.search_one(label=txt.lower())
            if (len(onto_c) == 0):
                onto_c = self.onto.search_one(label=txt.upper())
            if (len(onto_c) == 0):
                onto_c = self.onto.search_one(label=txt.title())
            print('get ', onto_c.label)
            list_subs(onto_c, sub)
            return [list(x)[0] for x in sub if len(x) > 0]
        except:
            try:
                onto_c = self.onto.search_one(iri=txt)
                list_subs(onto_c, sub)
                return [list(x)[0] for x in sub if len(x) > 0]
            except:
                print('can not find %s' % txt)
                pass

    def get_supers(self, txt):

        ''''return list of super classes'''

        print('matching sups of %s ' % txt)

        sup = []
        try:
            onto_c = self.onto.search_one(label=txt)
            if (onto_c == None):
                onto_c = self.onto.search_one(label=txt.lower())
            if (onto_c == None):
                onto_c = self.onto.search_one(label=txt.upper())
            if (onto_c == None):
                onto_c = self.onto.search_one(label=txt.title())

            list_supers(onto_c, sup)
            res = [list(x)[0] for x in sup if len(x) > 0]
            return res
        except:
            try:
                onto_c = self.onto.search_one(iri=txt)
                list_supers(onto_c, sup)
                return [list(x)[0] for x in sup if len(x) > 0]
            except:
                print('can not find %s' % txt)
                pass

    def sub_count(self, class_label):
        '''return subclass count'''
        print('counting %s subclass..' % class_label)

        res = self.get_subs(class_label)
        return len(res)

    def super_count(self, class_label):
        print('counting %s superclass..' % class_label)
        '''return superclass count'''
        res = self.get_supers(class_label)
        return len(res)

    def get_iri(self, class_label):
        try:
            onto_c = self.onto.search_one(label=class_label)
            # print('matching %s ..' %class_label)
            return onto_c.iri
        except:
            pass

    def get_factors(self, txt):
        try:
            onto_c = self.onto.search_one(label=txt)
            if (onto_c == None):
                onto_c = self.onto.search_one(label=txt.lower())
            if (onto_c == None):
                onto_c = self.onto.search_one(label=txt.upper())
            if (onto_c == None):
                onto_c = self.onto.search_one(label=txt.title())
            return list(onto_c.seeAlso)
        except:
            try:
                onto_c = self.onto.search_one(iri=txt)
                return list(onto_c.seeAlso)
            except:
                pass


def list_supers(onto_c, sup):
    if onto_c.label == '' or onto_c.iri == 'http://www.w3.org/2002/07/owl#Thing':
        return
    for parent in onto_c.is_a:
        try:
            list_supers(parent, sup)
            sup.append(parent.label)
        except:
            continue


def list_subs(onto_c, sub):
    if onto_c.label == '' or onto_c.iri == 'http://www.w3.org/2002/07/owl#Thing':
        return
    for children in onto_c.subclasses():
        try:
            list_subs(children, sub)
            sub.append(children.label)
        except:
            continue
