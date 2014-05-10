import random
import unittest


def insert(A,i):
    value = A[i]
    j = i
    while j != 0 and A[j-1]>value:
        A[j] = A[j-1]
        j = j - 1
    A[j] = value


def insertion_sort(A):
     for i in range(len(A)):
         insert(A, i)

class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        print "Setup ..."

    def testSortRange(self):
        print "TestSortRange .... \n"
        n = 10
        a = range(n)
        random.shuffle(a)
        insertion_sort(a)
        self.assertEqual(a, range(n))

        n = 1
        a = range(n)
        random.shuffle(a)
        insertion_sort(a)
        self.assertEqual(a, range(n))

        n = 77
        a = range(n)
        random.shuffle(a)
        insertion_sort(a)
        self.assertEqual(a, range(n))

    def testSortData(self):
        print "TestSortData .... \n"
        a = []
        r = []
        insertion_sort(a)
        self.assertEqual(a, r)

        a = [3, 1, 2]
        r = [1, 2, 3]
        insertion_sort(a)
        self.assertEqual(a, r)


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInsertionSort)
    unittest.TextTestRunner(verbosity=2).run(suite)