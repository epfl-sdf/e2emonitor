#!/usr/bin/env python
# -*-coding:Utf-8 -*
#lm261117.0138

# File to test scenario on service now

import numpy as np
import re
import time
import sys
sys.path.insert(0, '/home/ubuntu/e2emonitor/')
from credFinder import returnCred

from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def returnTimePoseidon():
	# Set screen resolution to 1920x 1080  like most laptops
	display = Display(visible=0, size=(1920, 1080))
	display.start()

	# now Firefox will run in a virtual display.
	profile = webdriver.FirefoxProfile()
	profile.native_events_enabled = True

	driver = webdriver.Firefox(profile)

	# Sets the width and height of the current window
	driver.set_window_size(1920, 1080)

	# Delete all cookies
	driver.delete_all_cookies()

	# Open the URL
	driver.get("https://it-test.epfl.ch/backoffice/login.do")
	driver.implicitly_wait(5)
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

	# Save timestamp
	timestamp = time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())

	# Go to poseidon page
	driver.get("https://it-test.epfl.ch/sc_task_list.do?sysparm_userpref_module=a3d5fe9509707900f03b46a6cae72c20&sysparm_view=Poseidon&sysparm$")
	driver.implicitly_wait(5)
	assert "Catalog Tasks" in driver.title

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "timing_network")))

	html_page = driver.page_source

	times = re.findall(r'Response time\(ms\): [0-9]*, Network: [0-9]*, server: [0-9]*, browser: [0-9]*', html_page)[0]
	all_times = re.findall(r'[0-9]+', times)

	driver.get("https://it-test.epfl.ch/backoffice/logout.do")

	# quit browser
	driver.quit()

	# quit Xvfb display
	display.stop()

	return timestamp, all_times
