#!/usr/bin/env python
# -*-coding:Utf-8 -*
#lm261117.0138

# File to test scenario on service now

import numpy as np
import sys
sys.path.insert(0, '/home/ubuntu/e2emonitor/')
from credFinder import returnCred

from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set screen resolution to 1920x 1080  like most laptops
display = Display(visible=0, size=(1920, 1080))
display.start()

# now Firefox will run in a virtual display.
driver = webdriver.Firefox()

# Sets the width and height of the current window
driver.set_window_size(1920, 1080)

# Open the URL
driver.get("https://it-test.epfl.ch/backoffice/login.do")
assert "Gestion des Services Informatiques" in driver.title

# Set up some credentials
(USER, PASS) = returnCred()
sys.path.remove('/home/ubuntu/e2emonitor/')

# Send user credential
user_name = driver.find_element_by_id("user_name")
user_name.send_keys(USER)

# Send password credential
user_password = driver.find_element_by_id("user_password")
user_password.send_keys(PASS)

# Uncheck "remember me"
checkBox = driver.find_element_by_id("remember_me")

if(checkBox.is_selected()):
	checkBox.click()

# Click login button
driver.find_element_by_id("sysverb_login").click()

# Go to poseidon page
driver.get("https://it-test.epfl.ch/sc_task_list.do?sysparm_userpref_module=a3d5fe9509707900f03b46a6cae72c20&sysparm_view=Poseidon&sysparm_query=request_item.cat_item=e7363462c92cb5005b9ed3385ccf2762%5eactive=true%5eEQ%27,%27All%20open%20incidents")
assert "Catalog Tasks" in driver.title

driver.get("https://it-test.epfl.ch/backoffice/logout.do")

# quit browser
driver.quit()

# quit Xvfb display
display.stop()
