from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time

class DragandDrop():

    def test1(self):
        baseUrl = "https://jqueryui.com/droppable/"
        # driver = webdriver.Firefox()
        # driver.maximize_window()
        # driver.get(baseUrl)
        driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
        os.environ["chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.switch_to.frame(0)

        #first method

        #Xpath not working to find the elemnt

        fromElement = driver.find_element(By.ID,"draggable")
        toElement = driver.find_element(By.ID,"droppable")

        actions = ActionChains(driver)
        # actions.drag_and_drop(fromElement,toElement).perform()

        #Second method

        actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()

        time.sleep(7)




ff = DragandDrop()
ff.test1()