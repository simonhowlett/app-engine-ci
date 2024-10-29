import unittest
import sys
import os
# from main import app
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helpers')))

def IsOdd(n):
    return n % 2 == 1

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testtwo(self):
        self.assertFalse(IsOdd(2))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
