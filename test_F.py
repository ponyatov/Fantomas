
import pytest

def test_none():
    assert False == False


from F import *

class TestObject:

    def test_hello(self):
        hello = Object('Hello')
        world = Object('World')
        left = Object('left')
        right = Object('right')
        assert (hello // world << left >> right).test() == \
            '\n<frame:Hello>\n\t'
