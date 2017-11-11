#!/usr/bin/env python
import numpy as np
import unittest

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

		# Set screen resolution to 1920x 1080  like most laptops
		display = Display(visible=0, size=(1920, 1080))
		display.start()

	def test_helloWorld_tequila(self):
		# now Firefox will run in a virtual display.
		driver = self.driver

		# Sets the width and height of the current window
		driver.set_window_size(1920, 1080)

		# Open the URL
		driver.get('128.178.116.97:8000')

		self.assertIn("Hello world", driver.title)
		elem_login = driver.find_element_by_link_text('Login')
		elem_login.click()

		# Login gaspard
		elem_username = Select(driver.find_element_by_id('username'))
		elem_username.send_keys("username")

		elem_password = Select(driver.find_element_by_id('password'))
		elem_password.send_keys("password")
		elem_password.send_keys(Keys.RETURN)

		driver.save_screenshot('test.png')
		# assert "No results found." not in driver.page_source

	def tearDown(self):
		# quit browser
		self.driver.close()

		# quit Xvfb display
		display.stop()

if __name__ == "__main__":
	unittest.main()
