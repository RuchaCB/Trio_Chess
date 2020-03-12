import unittest

from trial_refactor import *

class TestTrioChess(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testTrial(self): 
        self.assertEqual(4, 4)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
