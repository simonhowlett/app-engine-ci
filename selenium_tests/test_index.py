"""Local Homepage Tests

Confirms website is up and is serving content
Checks Alert Fires on selecting an image view button
Checks Debug content is hidden or available depending on URL params sent.

TODO: Lots of tests as needed, remote executing script, logging, etc etc.
Way too much repeated code...
"""

__version__ = 0.5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import time
import unittest
import sys

local_test = "http://127.0.0.1:8080"
prod_test = "https://durable-sunspot-277600.appspot.com"

# Provide a default value for sys.argv[1]
test_env = sys.argv[1] if len(sys.argv) > 1 else 'local'
test_url = prod_test if test_env == 'prod' else local_test

class TestIndex(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_homepage(self):
        self.driver.get(test_url)
        self.assertIn("Homepage", self.driver.title)

if __name__ == '__main__':
    unittest.main()
