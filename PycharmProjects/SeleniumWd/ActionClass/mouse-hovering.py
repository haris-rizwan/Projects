from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time

class MouseHovering():

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        # driver = webdriver.Firefox()
        # driver.maximize_window()
        # driver.get(baseUrl)
        driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
        os.environ["chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        # try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print("Mouse Hovered on element")
        time.sleep(5)
        topLink = driver.find_element(By.XPATH, itemToClickLocator)
        actions.move_to_element(topLink).click().perform()
        print("Item Clicked")
        # except:
        #     print("Mouse Hover failed on element")

ff = MouseHovering()
ff.test1()