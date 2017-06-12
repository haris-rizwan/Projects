from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Mousehovering():

    def __init__(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
        os.environ["chrome.driver"] = driverLocation
        self.driver = webdriver.Chrome(driverLocation)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(baseUrl)



    def  Hover(self):
        self.driver.execute_script("window.scrollBy(0,800)")
        element = self.driver.find_element(By.ID,"mousehover")
        topLink = self.driver.find_element(By.XPATH,"//div[@class='mouse-hover']//a[contains (text(),'Top')]")

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(3)
        actions.move_to_element(topLink).click().perform()
        time.sleep(2)

        self.driver.quit()

ff = Mousehovering()
ff.Hover()



















