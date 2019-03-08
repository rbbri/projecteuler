import unittest
from multiplesof3and5 import *

class Tests(unittest.TestCase):

    def test_multiple_of(self):
        self.assertEqual( multiple_of(9, 3), True )
        self.assertEqual( multiple_of(10, 3), False )
        self.assertEqual( multiple_of(10,5), True )
        self.assertEqual( multiple_of(11, 5), False )

    def test_solution(self):
        self.assertEqual( solution(), '233168')

if __name__ == '__main__':
    unittest.main()
