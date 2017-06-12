from selenium import webdriver

import os

class ChromeTest():

    def test(self):
        driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
        os.environ["webdriver.chrome.driver"]= driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://www.google.ca")


cTest = ChromeTest()

cTest.test()