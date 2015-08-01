__author__ = 'apatti'

class fwrapper:

    def __init__(self, function, childcount, name):
        self.function = function
        self.childcount = childcount
        self.name = name


class node:

    def __init__(self, fw, children):
        self.function = fw.function
        self.children = children
        self.name = fw.name

    def evaluate(self, inp):
        results = [n.evaluate(inp) for n in self.children]

        return self.function(results)

    def display(self, indent=0):
        print '%s%s' % (' '*indent, self.name)
        [child.display(indent+1) for child in self.children]


class paramnode:

    def __init__(self, idx):
        self.idx = idx

    def evaluate(self, inp):
        return inp[self.idx]

    def display(self, indent=0):
        print '%sp%d' % (' ' * indent, self.idx)


class constnode:

    def __init__(self, value):
        self.value = value

    def evaluate(self, inp):
        return self.value

    def display(self, indent):
        print '%s%d' % (' ' * indent, self.value)

