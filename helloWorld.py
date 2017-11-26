#!/usr/bin/env python
# -*-coding:Utf-8 -*

import numpy as np
import credFinder

from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Set up some credentials variables
(USER, PASS) = credFinder.returnCred()

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
#assert "Login" in driver.title

# Login gaspard
elem_username = driver.find_element_by_id("username")
elem_username.send_keys(USER)

elem_password = driver.find_element_by_id("password")
elem_password.send_keys(PASS)

elem_buttonLoggin = driver.find_element_by_id("loginbutton")
elem_buttonLoggin.click()
#assert "Logged" in driver.find_element_by_tag_name("h1")

elem_list_shoes = driver.find_element_by_link_text("Liste des chaussures")
elem_list_shoes.click()
#assert "Marque" in driver.find_element_by_tag_name("h1")

elem_add_shoe = driver.find_element_by_link_text("Add Shoe")
elem_add_shoe.click()
#assert "Brand" in driver.find_element_by_tag_name("h1")

driver.find_element_by_id("id_brand").send_keys("LM_asics")
driver.find_element_by_id("id_size").send_keys("11")
driver.find_element_by_id("id_color").send_keys("Ro")
driver.find_element_by_id("id_shoe_type").send_keys("Co")
driver.find_element_by_xpath("//input[@value='Submit'][@type='submit']").click()

driver.find_element_by_link_text("Logout").click()

# quit browser
driver.close()

# quit Xvfb display
display.stop()
