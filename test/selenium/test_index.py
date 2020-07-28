"""Local Homepage Tests

Confirms website is up and is serving content
Checks Alert Fires on selecing an image view button
Checks Debug content is hidden or available depending on URL params sent.

TODO: Lots of tests as needed, remote executing script, logging, etc etc.
Way too much repeated code...
"""

__version__ = 0.3

import unittest
import datetime
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_url = "http://127.0.0.1:8080/"
debug_url = test_url + "?debug=true"


class TestsHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        global driver
        driver = self.driver
        driver.get(test_url)
        global tStart
        tStart = time()
        global tEnd
        tEnd = time()

    def test_title_content(self):
        ''' Tests initial album page is loaded, and content is present'''
        self.assertIn("Homepage", driver.title)
        footer = self.driver.find_element_by_link_text("Back to top")
        self.assertTrue(footer.is_displayed())
        content = self.driver.find_element_by_id('paris_01')
        self.assertTrue(content.is_displayed())

    def test_menu_access(self):
        ''' Tests drop down menu doesn't break'''
        driver.find_element_by_class_name('navbar-toggler-icon').click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "links_menu"))
            )
        finally:
            menu_open = driver.find_element_by_id('links_menu')
            self.assertTrue(menu_open.is_displayed())

    def test_select_image_alert(self):
        ''' Tests alert fires'''
        driver.find_element_by_id('la_2019').click()
        alert_obj = driver.switch_to.alert
        self.assertEqual('Intentionally Not Yet wired up', alert_obj.text)
        alert_obj.accept()

    def test_select_image_caption(self):
        ''' Tests Query String for Caption is being passed and loaded'''
        driver.find_element_by_id('paris_01').click()
        self.assertIn("Full Size Image", driver.title)
        caption = driver.find_element_by_name('caption')
        self.assertEqual('Unknown, Paris, 2018', caption.text)
        driver.find_element_by_name('back_to_home').click()
        self.assertIn("Homepage", driver.title)

    def test_debug(self):
        '''Tests Debug Text Appears in debug mode'''
        driver.get(debug_url)
        debug_content = driver.find_element_by_class_name('hideme')
        self.assertTrue(debug_content.is_displayed())

    def test_not_debug(self):
        '''Tests Debug Text hidden in normal use'''
        debug_content = driver.find_element_by_class_name('hideme')
        self.assertFalse(debug_content.is_displayed())

    def tearDown(self):
        tEnd = time()
        time_span = tEnd - tStart
        print(f'Test: {self} took {time_span} seconds duration')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
