import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helpers')))

# from main import app
from test import to_test
class TestMain(unittest.TestCase):
    
    def test_do_stuff(self):
        test_param = 10
        result = to_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shshssh'
        result = to_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

if __name__ == '__main__':
    unittest.main()
