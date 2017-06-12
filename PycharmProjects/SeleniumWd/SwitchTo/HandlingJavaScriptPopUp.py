from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JsPopUp():
    def __init__(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.get(baseUrl)

    def JavaScriptPop(self):
        Name = self.driver.find_element(By.ID, "name")
        Name.send_keys("Haris")
        # alertbutton
        self.driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        # switch to alert frame
        self.driver.switch_to_alert().accept()
        #to cancel jave pop up
        #self.driver.switch_to_alert().dismiss()

        #the alert will only work for javascripy popups

    def Test(self):
        self.JavaScriptPop()


ff = JsPopUp()
ff.Test()
