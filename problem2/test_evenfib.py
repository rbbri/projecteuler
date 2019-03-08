import unittest
from evenfib import *

class Tests(unittest.TestCase):

    def test_solution(self):
        self.assertEqual( solution(), '4613732' )

if __name__ == '__main__':
    unittest.main()
