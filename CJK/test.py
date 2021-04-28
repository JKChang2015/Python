# -*- coding: UTF-8 -*-
# File name: test
# Created by JKChang
# 29/08/2020, 14:05
# Tag:
# Description: inter test

import pandas as pd
import numpy as np

from collections import defaultdict


def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following
      elements: Class name (string), median grade for students in the class (float).
    """

    dict_ = defaultdict(list)

    for student in students:
        dict_[student[1]].append(student[2])

    res = []

    for k, v in dict_.items():
        res.append([k, np.median(v)])

    return res


students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
print(class_grades(students))