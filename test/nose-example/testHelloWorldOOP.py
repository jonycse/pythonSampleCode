__author__ = 'AbuZahedJony'

from helloWorld import add_two_num
from helloWorld import multi_two_num

'''
nosetests testHelloWorld.py
nosetests -s testHelloWorld.py # show log
'''

class TestHelloWorld:
    def __init__(self):
        pass

    # This function will run before any test case (only once)
    @classmethod
    def setup_class(cls):
        print "Main Setup"

    # This function will run after all test case (only once)
    @classmethod
    def teardown_class(cls):
        print "Main Teardown"

    # This function will call per test case (before)
    def setup(self):
        print "SETUP"

    # This function will call per test case (after)
    def teardown(self):
        print "TEAR-DOWN"

    def test_add_num(self):
        print 10*"*"+" Test add num"
        assert add_two_num(2, 3) == 5
        assert add_two_num(-2, 3) == 1

    def test_multi_num(self):
        print 10*"*"+" Test multi num"
        assert multi_two_num(2, 3) == 6
        assert multi_two_num(-2, 3) == -6