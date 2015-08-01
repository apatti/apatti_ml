__author__ = 'apatti'

from gptree import fwrapper, constnode, node, paramnode


class mathpoc:

    def __init__(self):
        def iffunc(i):
            if i[0] > 0:
                return i[1]
            else:
                return i[2]

        def greater(i):
            if i[0] > i[1]:
                return 1
            else:
                return 0

        addw = fwrapper(lambda i: i[0]+i[1], 2, 'add')
        subw = fwrapper(lambda i: i[0]-i[1], 2, 'sub')
        greatw = fwrapper(greater, 2, '>')
        ifw = fwrapper(iffunc, 3, 'if')

        self.flist=[addw, subw, greatw, ifw]


