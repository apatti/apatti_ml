__author__ = 'apatti'

import unittest
from gptree import fwrapper, constnode, node, paramnode


class gbtree_test_case(unittest.TestCase):
    def test_complex_tree(self):
        print 'test_complex_tree'

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

        tree = node(ifw, [node(greatw, [paramnode(0), constnode(3)]),
                          node(addw, [paramnode(1), constnode(5)]),
                          node(subw, [paramnode(1), constnode(2)])])
        tree.display(2)

        self.assertEqual(tree.evaluate([2, 3]), 1)
        self.assertEqual(tree.evaluate([5, 3]), 8)


if __name__ == '__main__':
    unittest.main()
