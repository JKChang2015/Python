# -*- coding: utf-8 -*-
# multiplication table
for i in range(1, 10):
    for j in range(1, 10):
        if (i >= j):
            print j, "x", i, "=", i * j, '\t',
    print
