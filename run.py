#!/usr/bin/env python
# Author Dinuka Salwathura
# Hybriteq Inc
# To run this script selenium pip module has to be installed

# API Docs http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

############################### DRIVER 1
browser = webdriver.Firefox()
browser.set_window_size(500,700)
browser.get('http://localhost:8100')

elem=browser.find_element_by_id("email")
elem.send_keys("sala@gmail.com")

elem=browser.find_element_by_id("password")
elem.send_keys("123456")

# set gps location

latitude="6.0419023"
longitude="80.2417354"

SPOOF_LOCATION_JS = """
(function() {
console.log('Preparing geo spoofing');
navigator.geolocation.getCurrentPosition = function(success) {
    console.log("getCurrentPosition() called");
    setTimeout(function() { console.log("Sending out fake coordinates"); success({coords: {latitude: """+latitude+""", longitude: """+longitude+"""}}); }, 500);
};
console.log("Finished geospoofing")})();
"""

browser.execute_script(SPOOF_LOCATION_JS.replace("\n", " "))

elem=browser.find_element_by_id("login")
elem.click()
#browser.refresh()

try:
    elem= WebDriverWait(browser,30).until(
        EC.presence_of_element_located((By.ID,"toggle-0-0"))
    )
finally:
    #elem=browser.find_element_by_id("toggle-0-0")
    elem.click()
