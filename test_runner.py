'''Building out a test runner app

'''

import unittest
loader = unittest.TestLoader()
start_dir = 'test/selenium'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
