"""Initial Test

Confirms website is up and is serving content
Checks Alert Fires on selecing an image view button
Currently these use a local webdriver instance, remote scripts will follow.

TODO: Lots of tests as needed, remote executing script, logging, etc etc.
"""

__version__ = 0.1

import unittest
import time
import os
import sys
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# Local Url http://127.0.0.1:8080/
# App Engine Url: TODO

test_url = "http://127.0.0.1:8080/"


class simple_tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title_content(self):
        driver = self.driver
        driver.get(test_url)
        self.assertIn("Homepage", driver.title)

    def test_select_image_alert(self):
        driver = self.driver
        driver.get(test_url)
        driver.find_element_by_id('la_2019').click()
        alert_obj = driver.switch_to.alert
        self.assertEqual('Not Yet wired up', alert_obj.text)
        alert_obj.accept()

    def test_select_image_caption(self):
        ''' Tests Query String for Caption is being passed and loaded

        '''
        driver = self.driver
        driver.get(test_url)
        driver.find_element_by_id('paris_01').click()
        self.assertIn("Full Size Image", driver.title)
        caption = driver.find_element_by_name('caption')
        self.assertEqual("'Unknown, Paris, 2018'", caption.text)
        driver.find_element_by_name('back_to_home').click()
        self.assertIn("Homepage", driver.title)

        # TODO - Image URL check via parmameter
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


# next lines run the tests as a suite, outputting each test's results.
suite = unittest.TestLoader().loadTestsFromTestCase(simple_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

# run from command line, replace the commented lines with those above
# if __name__ == "__main__":
#     unittest.main()