
import os, sys

class Object:               # Frame see Marvin Minsky
    def __init__(self, V):
        self.val = V        # scalar value
        self.slot = {}      # attributes = dict = env
        self.nest = []      # nested elements = AST = vector = stack = queue

    ## dump

    def __repr__(self): return self.dump()
    def test(self): return self.dump(test=True)

    def dump(self, depth=0, prefix='', test=False):
        tree = self._pad(depth) + self.head(prefix, test)
        # slot{}s
        for i in self.slot:
            tree += self.slot[i].dump(depth + 1, '%s = ' % i, test)
        # nest[]ed
        idx = 0
        for j in self.nest:
            tree += j.dump(depth + 1, '%s: ' % idx, test)
            idx += 1
        return tree

    def head(self, prefix='', test=False):
        hdr = '%s<%s:%s>' % (prefix, self._type(), self._val())
        if not test:
            hdr += ' @%x' % id(self)
        return hdr

    def _pad(self, depth): return "\n" + "\t" * depth

    def _type(self): return self.__class__.__name__.lower()
    def _val(self): return '%s' % self.val

    ## operators

    def __getitem__(self, key):
        return self.slot[key]

    def __setitem__(self, key, that):
        self.slot[key] = that
        return self

    def __lshift__(self, that):
        return self.__setitem__(that._type(), that)

    def __rshift__(self, that):
        return self.__setitem__(that._val(), that)

    def __floordiv__(self, that):
        self.nest.append(that)
        return self
