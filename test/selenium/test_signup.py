"""Initial Local Tests

Confirms Signup page is loaded, fields can be completed
Confirms password validation is working on identical values.

TODO: Commit Test Status and Timings to Cloud datastore,
remote executing script, logging, etc etc.
"""

__version__ = 0.3

import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from time import time

test_url = "http://127.0.0.1:8080/info"
debug_url = test_url + "?debug=true"
start_time = datetime.datetime.now()


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(test_url)
        global driver
        driver = self.driver
        global tStart
        tStart = time()
        global tEnd
        tEnd = time()

    def test_pwd_match_continue(self):

        self.assertIn(
            "Street art photos by Simon Howlett- Info Sign Up", driver.title)
        firstName = self.driver.find_element_by_name(
            'firstName').send_keys('tester')
        lastName = self.driver.find_element_by_name(
            'lastName').send_keys('testing')
        email = self.driver.find_element_by_name(
            'email').send_keys('testing@test.com')
        pwd = self.driver.find_element_by_name('pwd')
        pwd.send_keys('8ightChar')
        cnf_pwd = self.driver.find_element_by_name('cnf_pwd')
        cnf_pwd.send_keys('8ightchar')
        submit = self.driver.find_element_by_name('submit')
        submit.click()
        alert_obj = driver.switch_to.alert
        self.assertEqual(
            '\nPassword did not match: Please try again...', alert_obj.text)
        alert_obj.accept()
        pwd.clear()
        cnf_pwd.clear()
        pwd.send_keys('8ightChar')
        cnf_pwd.send_keys('8ightChar')
        submit.click()
        self.assertIn(
            "Street art photos by Simon Howlett- Signed Up!", driver.title)

    def tearDown(self):
        tEnd = time()
        time_span = tEnd - tStart
        print('Started', start_time)
        print(f'Test: {self} took {time_span} seconds duration')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
