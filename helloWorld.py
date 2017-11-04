#!/usr/bin/env python
import numpy as np

from pyvirtualdisplay import Display
from selenium import webdriver

# Set screen resolution to 1920x 1080  like most laptops
display = Display(visible=0, size=(1920, 1080))
display.start()

# now Firefox will run in a virtual display.
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.http', 'http://e2e-louis-1.sdftests.xyz:8000')
profile.set_preference('network.proxy.http_port', 8000)
    
browser = webdriver.Firefox(profile)

# Sets the width and height of the current window
browser.set_window_size(1920, 1080)

# Open the URL
browser.get('http://e2e-louis-1.sdftests.xyz:8000')

# set timeouts
browser.set_script_timeout(30)
browser.set_page_load_timeout(30) # seconds

# Take screenshot
browser.save_screenshot('helloWorld.png')

# quit browser
browser.quit()

# quit Xvfb display
display.stop()
