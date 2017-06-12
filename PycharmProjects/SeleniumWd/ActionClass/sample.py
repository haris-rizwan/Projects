from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time


class Slider():
    def test1(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        # driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
        # os.environ["chrome.driver"] = driverLocation
        # driver = webdriver.Chrome(driverLocation)
        # driver.implicitly_wait(5)
        # driver.maximize_window()
        driver.get(baseUrl)

        driver.switch_to.frame(0)

        Slider = driver.find_element(By.XPATH,"//div[@id='slider']//span")
        time.sleep(3)



ff = Slider()

ff.test1()