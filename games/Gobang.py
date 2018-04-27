# GoBang
# Created by JKChang
# 18/04/2018, 09:54
# Tag:
# Description:

# ! /usr/bin/env python
# -*- coding: utf-8 -*-

class chessboard(object):

    def __init__(self, forbidden=0):
        self.__board = [[0 for n in range(15)] for m in range(15)]
        self.__forbidden = forbidden
        self.__dirs = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
        self.DIRS = self.__dirs
        self.won = {}

    def reset(self):
        for j in range(15):
            for i in range(15):
                self.__board[i][j] = 0
        return 0

    def __getitem__(self, row):
        return self.__board[row]

    def __str__(self):
        text = '  A B C D E F G H I J K L M N O\n'
        mark = ('. ', 'O ', 'X ')
        nrow = 0
        for row in self.__board:
            line = ''.join([mark[n] for n in row])
            text += chr(ord('A') + nrow) + ' ' +line
            nrow+=1
            if nrow < 15: text += '\n'
        return text


