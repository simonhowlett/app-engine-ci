"""Initial Tests

Confirms Signup page is loaded
Confirms fields can be completed
Confirms password validation is working on identical values.
Currently these use a local webdriver instance, remote scripts will follow.

TODO: Commit Test Status and Timings to Cloud datastore,
remote executing script, logging, etc etc.
"""

__version__ = 0.2

import unittest
import os
import sys
import re
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


class simple_tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_pwd_match_continue(self):
        driver = self.driver
        driver.get(test_url)
        self.assertIn("Street art - Info", driver.title)
        tStart = time()
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
        self.assertIn("Street art - Signed Up!", driver.title)
        tEnd = time()
        time_span = tEnd - tStart
        print('Started', start_time)
        print(f'Test: {self} took {time_span} seconds duration')

    # def store_time(dt):
        # entity = datastore.Entity(key=datastore_client.key('test_time'))
        # entity.update({
        #     'timestamp': start_time,
        #     'testname': unittest.TestCase,
        #     'timeSpan': time_span
        #     })
        # datastore_client.put(entity)

    def tearDown(self):
        self.driver.close()


# next lines run the tests as a suite, outputting each test's results.
# suite = unittest.TestLoader().loadTestsFromTestCase(simple_tests)
# unittest.TextTestRunner(verbosity=2).run(suite)

# run from command line, replace the commented lines with those above
if __name__ == "__main__":
    unittest.main()
