'''Building out a test runner wrapper

'''

import unittest
loader = unittest.TestLoader()
start_dir = 'selenium_tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
