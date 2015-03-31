from nose import with_setup

__author__ = 'AbuZahedJony'

'''
nosetests testHelloWorld.py
nosetests -s testHelloWorld.py # show log
'''

from helloWorld import add_two_num
from helloWorld import multi_two_num


def m_setup():
    print "\nRun SETUP"


def m_teardown():
    print "Run TEAR-DOWN"



@with_setup(m_setup, m_teardown)
def test_add_num():
    print "Running test ADD"
    assert add_two_num(2, 3) == 5
    assert add_two_num(-2, 3) == 1
    assert add_two_num(-2, -3) == -5



@with_setup(m_setup, m_teardown)
def test_multi_num():
    print "Running test MULTI"
    assert multi_two_num(2, 3) == 6
    assert multi_two_num(-2, 3) == -6
    assert multi_two_num(-2, -3) == 6

