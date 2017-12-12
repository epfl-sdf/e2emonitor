#!/usr/bin/env python
# -*-coding:Utf-8 -*
#lm261117.0138

# File to test scenario on is-academia

import time

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
driver.get("https://isatest.epfl.ch/imoniteur_ISAT/!gedpublicreports.htm?ww_i_reportmodel=66627699")
assert "IS-Academia - TEST" in driver.title

# First we have to switch to the frame which content the form
frame = driver.find_element_by_xpath('//frame[@name="toc"]')
driver.switch_to.frame(frame)

# Select HTML option format
driver.find_element_by_xpath("//input[@value='66627723']").click()

# Select 2017-2018 academic year
anneeAcad = driver.find_element_by_name("ww_x_PERIODE_ACAD")
anneeAcad.send_keys("2017")

# Select automn semester
Select(driver.find_element_by_name("ww_x_HIVERETE")).select_by_visible_text("Semestre d'automne")

# Keep course empty
# Select classe
Select(driver.find_element_by_name("ww_x_CLASSE")).select_by_visible_text("CMS 1/3 Automne")

# Select ok and then click on it
okButton = driver.find_element_by_name("dummy")
okButton.click()

driver.save_screenshot("test_ok.png")

# Select Algebre lineaire pour CMS
WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td/a"))
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td/a").click()

# Change frame that we focuse on
driver.switch_to_default_content()
frame = driver.find_element_by_name("principal")
driver.switch_to.frame(frame)

# Test if we have data
text_found = re.search(r'Semestre.automne', driver.page_source)

time.sleep(5)
driver.save_screenshot("test_list.png")

# quit browser
driver.quit()

# quit Xvfb display
display.stop()
