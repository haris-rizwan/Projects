from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time

class Contobox1():

    def Test1(self):

       baseUrl = "http://srv1.contobox.com/v3/preview.php?id=14196"
       driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
       os.environ["chrome.driver"] = driverLocation
       driver = webdriver.Chrome(driverLocation)
       driver.implicitly_wait(5)
       driver.maximize_window()
       driver.get(baseUrl)
       time.sleep(1)
       preBanner = driver.find_element(By.CLASS_NAME,"cb-321-container")
       preBanner.click()
       actions = ActionChains(driver)
       actions.move_to_element(preBanner).click(preBanner).perform()





ff = Contobox1()

ff.Test1()