#!/usr/bin/env python
import numpy as np

from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Set screen resolution to 1920x 1080  like most laptops
display = Display(visible=0, size=(1920, 1080))
display.start()

# now Firefox will run in a virtual display.
driver = webdriver.Firefox()

# Sets the width and height of the current window
driver.set_window_size(1920, 1080)

# Open the URL
driver.get("http://e2e-louis-1.sdftests.xyz:8000")

assert "Hello world" in driver.title
elem_login = driver.find_element_by_link_text("Login")
elem_login.click()

# Login gaspard
elem_username = driver.find_element_by_id("username")
elem_username.send_keys("username")

elem_password = driver.find_element_by_id("password")
elem_password.send_keys("password")
elem_password.send_keys(Keys.RETURN)
assert "Logged" in driver.title

driver.save_screenshot("test.png")
# assert "No results found." not in driver.page_source

# quit browser
self.driver.close()

# quit Xvfb display
display.stop()
