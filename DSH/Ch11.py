# Ch11
# Created by JKChang
# 10/01/2018, 10:00
# Tag:
# Description: testing

import unittest
# tutorial video:https://www.youtube.com/watch?v=6tNS--WetLI
# http://pythonguidecn.readthedocs.io/zh/latest/writing/tests.html


def get_formatted_name(first, last):
    ''''generate a neatly formatted name'''
    full_name = first.title() + ' ' + last.title()
    print(full_name)
    return full_name


class NamesTestCase(unittest.TestCase):
    '''test get_formatted_name'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('david', 'Ch')
        self.assertEqual(formatted_name, 'David Ch')

