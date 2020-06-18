"""Initial Test

Confirms website is up and is serving content
"""

__version__ = 0.1

import unittest
from selenium import webdriver

# Local Url http://127.0.0.1:8080/
# App Engine Url: 
 
class startUpTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title_content(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8080/")
        self.assertIn("Homepage", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()