---
layout: post
title: Testing with Selenium
slug: testing-with-selenium
author: Martin Thoma
status: draft
date: 2017-08-29 20:00
category: Testing
tags: Selenium, Testing, Python
featured_image: logos/selenium.png
---


## Basic example

From [How do I write a Python Selenium test script that contains more than one test case?](https://stackoverflow.com/q/20515676/562769):

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class AdminTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mysite.local"

    def test_discount_test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/login")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("p@ssw0rd")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//li[4]/a/span").click()
        driver.find_element_by_link_text("Add Discount").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Selenium Test Discount")
        driver.find_element_by_name("body").clear()
        driver.find_element_by_name("body").send_keys("Test discount text")
        driver.find_element_by_name("start_date").clear()
        driver.find_element_by_name("start_date").send_keys("01/01/2014")
        driver.find_element_by_name("end_date").clear()
        driver.find_element_by_name("end_date").send_keys("01/03/2014")
        driver.find_element_by_name("discount_percentage").clear()
        driver.find_element_by_name("discount_percentage").send_keys("33")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def test_add_unit_type(self):
        driver = self.driver
        driver.get(self.base_url + "/maxsys/unit_types")
        driver.find_element_by_link_text("Add Unit type").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Selenium Test Unit Type")
        driver.find_element_by_name("height").clear()
        driver.find_element_by_name("height").send_keys("22.5")
        driver.find_element_by_name("width").clear()
        driver.find_element_by_name("width").send_keys("Non-numeric")
        driver.find_element_by_name("depth").clear()
        driver.find_element_by_name("depth").send_keys("Test discount text")
        driver.find_element_by_name("body").clear()
        driver.find_element_by_name("body").send_keys("unit type description")
        driver.find_element_by_xpath("//button[@type='submit']").click()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

if __name__ == "__main__":
    unittest.main()

```


## See also

* StackOverflow:
    * [Why do assertions in unittest use TestCase.assertEqual not the assert keyword?](https://stackoverflow.com/q/6361147/562769)
* http://www.techbeamers.com/selenium-python-test-suite-unittest/#h1.1
