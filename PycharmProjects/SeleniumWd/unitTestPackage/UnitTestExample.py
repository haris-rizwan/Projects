from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import unittest

class TestingPackageExample(unittest.TestCase):

    # def __init__(self):
    #     baseUrl = "https://letskodeit.teachable.com/p/practice"
    #     self.driver = webdriver.Firefox()
    #     # self.driver.maximize_window()
    # #     # time.sleep(4)
    #     self.driver.get(baseUrl)

    @classmethod
    def setUpClass(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.get(baseUrl)

    def test_EnterName(self):
        name = self.driver.find_element(By.XPATH,"//input[@id='name']")
        name.send_keys("Haris Rizwan")
        time.sleep(6)

    def test_Clickconfirm(self):
        confirm = self.driver.find_element(By.XPATH,"//input[@id='confirmbtn']")
        confirm.click()
        time.sleep(3)

    def test_JavaPopupclose(self):
         self.driver.switch_to_alert().dismiss()
         time.sleep(5)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


