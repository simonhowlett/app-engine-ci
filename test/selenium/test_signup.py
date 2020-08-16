"""Initial Local Tests

Confirms Signup page is loaded, fields can be completed
Confirms password validation is working on identical values.

TODO: Commit Test Status and Timings to Cloud datastore,
remote executing script, logging, etc etc.
"""

__version__ = 0.4

import sys
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

local_test = "http://127.0.0.1:8080/info"
prod_test = "https://durable-sunspot-277600.appspot.com/info"
test_url = prod_test if sys.argv[1] == 'prod' else local_test

debug_url = test_url + "?debug=true"
start_time = datetime.datetime.now()


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        global driver
        driver = self.driver
        driver.get(test_url)
        driver.maximize_window()
        global tStart
        tStart = time()
        global tEnd
        tEnd = time()

    def test_success_submit(self):

        self.assertIn(
            "Street art photos by Simon Howlett- Contact me", driver.title)
        name = driver.find_element_by_name(
            'name').send_keys('tester mctesterson')
        email = driver.find_element_by_name(
            'email').send_keys('testing@test.com')
        email2 = driver.find_element_by_name(
            'email2').send_keys('testing@test.com')
        comment = driver.find_element_by_name('comment').send_keys('Funky Cold Medina')
        submit = driver.find_element_by_name('submit')
        submit.click()
        # conf_msg = driver.find_element_by_id('conf_msg')
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "conf_msg")))
        finally:
                self.assertIn("Street art photos by Simon Howlett- Thanks for your message!", driver.title)

    def tearDown(self):
        tEnd = time()
        time_span = tEnd - tStart
        print('Started', start_time)
        print(f'Test: {self} took {time_span} seconds duration')
        driver.close()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
