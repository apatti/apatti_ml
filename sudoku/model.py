__author__ = 'apatti'

import numpy as np


class sModel:

    def __init__(self):
        self.__table = np.zeros(shape=(3, 3, 3, 3), dtype=int)
        self.__tofill = range(0, 81)

    def display(self):
        print self.__table

    def writerow(self, row, numbers):
        colindex=0
        tableindex=row/3
        for index, number in enumerate(numbers):
            self.__table[tableindex, colindex, row % 3, index % 3] = number
            if number != 0:
                self.__tofill.remove((row * 9) + index)

            if index % 3 == 2:
                colindex += 1

    def getrow(self, row):
        a = (row / 3)%3
        b = row % 3
        return self.__table[a, :, b, :]

    def getadjacentrow(self,position):
        currentrow = position % 9
        adjacent = []
        if currentrow % 3 == 0:
            adjacent.extend(self.getrow(currentrow+1).flatten().tolist())
            adjacent.extend(self.getrow(currentrow+2).flatten().tolist())
        if currentrow % 3 == 1:
            adjacent.extend(self.getrow(currentrow-1).flatten().tolist())
            adjacent.extend(self.getrow(currentrow+1).flatten().tolist())
        if currentrow % 3 == 2:
            adjacent.extend(self.getrow(currentrow-1).flatten().tolist())
            adjacent.extend(self.getrow(currentrow-2).flatten().tolist())

        adjacent = list(set(adjacent))
        adjacent.remove(0)
        return adjacent

    def getcol(self, col):
        a = (col/3) % 3
        b = col % 3
        return self.__table[:, a, :, b]

    def getadjacentcol(self,position):
        currentcol = position % 9
        adjacent = []
        if currentcol % 3 == 0:
            adjacent.extend(self.getrow(currentcol+1).flatten().tolist())
            adjacent.extend(self.getrow(currentcol+2).flatten().tolist())
        if currentcol % 3 == 1:
            adjacent.extend(self.getrow(currentcol-1).flatten().tolist())
            adjacent.extend(self.getrow(currentcol+1).flatten().tolist())
        if currentcol % 3 == 2:
            adjacent.extend(self.getrow(currentcol-1).flatten().tolist())
            adjacent.extend(self.getrow(currentcol-2).flatten().tolist())

        adjacent = list(set(adjacent))
        adjacent.remove(0)
        return adjacent

    def getblock(self, block):
        a = block/3
        b = block % 3
        return self.__table[a, b, :, :]

    def getpeers(self,position):
        # row, col and block
        row = position / 9
        col = position % 9
        block = (row/3)*3+col/3
        peers = self.getcol(col).flatten().tolist()
        peers.extend(self.getrow(row).flatten().tolist())
        peers.extend(self.getblock(block).flatten().tolist())
        peers = list(set(peers))
        peers.remove(0)
        return peers

    def getpossiblenumbers(self,position):
        peers = self.getpeers(position)
        #peers.extend(self.getadjacentcol(position))
        #peers.extend(self.getadjacentrow(position))
        return list(set(range(1, 10)) - set(peers))

    def __solvesimple(self):
        # take each zero number box in row and check what all can fit.
        for position in self.__tofill:
            print position,self.getpossiblenumbers(position)
        pass


    def solve(self):
        self.__solvesimple()