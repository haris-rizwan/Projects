from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver import ActionChains
import os
import time

class TestingExamplePackage2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
        os.environ["chrome.driver"] = driverLocation
        self.driver = webdriver.Chrome(driverLocation)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(baseUrl)
        self.driver.switch_to.frame(0)
        time.sleep(2)

    # def test_switchtoIframe(self):
    #     self.driver.switch_to.frame(0)
    #     time.sleep(4)

    def test_findElement(self):
        time.sleep(5)
        fromElement = self.driver.find_element(By.ID, "draggable")
        toElement = self.driver.find_element(By.ID, "droppable")
        actions = ActionChains(self.driver)
        actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
        time.sleep(5)


       # how to use element from one method in an other method ?????

    # def test_performDragandDrop(self):
    #     actions = ActionChains(self.driver)
    #     actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)