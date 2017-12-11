#!/usr/bin/env python
# -*-coding:Utf-8 -*
#lm261117.0138

# File to test scenario on is-academia

import re

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
driver.get("http://isatest.epfl.ch/imoniteur_ISAT/!GEDPUBLICREPORTS.htm?ww_i_reportModel=2096516523")
assert "IS-Academia - TEST" in driver.title

# First we have to switch to the frame which content the form
frame = driver.find_element_by_xpath('//frame[@name="toc"]')
driver.switch_to.frame(frame)

# Select PDF option format
driver.find_element_by_xpath("/html/body/div[2]/form/table[1]/tbody/tr[3]/td/input").click()

# Select 2017-2018 academic plan
Select(driver.find_element_by_name("ww_x_PLANMODELE")).select_by_visible_text("Informatique 2017-18")

# Select automn semester
Select(driver.find_element_by_name("ww_x_HIVERETE")).select_by_visible_text("Semestre d'automne")

# Keep date empty

# Select ok and then click on it
okButton = driver.find_element_by_name("dummy")
okButton.click()

driver.save_screenshot("test.png")

# Select Algebre lineaire pour CMS
WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[5]/td/a"))
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[5]/td/a").click()

# Change frame that we focuse on
driver.switch_to_default_content()
frame = driver.find_element_by_name("principal")
driver.switch_to.frame(frame)

# quit browser
driver.quit()

# quit Xvfb display
display.stop()
