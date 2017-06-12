from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import os
from selenium.common.exceptions import *

baseUrl = "https://srv1.contobox.com/v3/preview.php?id=14240"

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(baseUrl)

mainpage=driver.current_window_handle

#it will first go to the pre banner expansion iframe a
frame1 = driver.find_element(By.TAG_NAME,"iframe")
value=frame1.get_attribute("id")
driver.switch_to.frame(value)
print(value)
# after that it will go find the element of pre banner and click it
banner=driver.find_element(By.ID,"cb-ctr")
banner.click()
time.sleep(3)


driver.switch_to.default_content()
driver.switch_to.frame(1)

tb = driver.find_elements(By.XPATH,".//div[@id='layout-tabs']/div")
print(len(tb))

screens="/Users/harisrizwan/Desktop/Selenium screen shots/test.png"

if tb is not None:
    for i in tb:
        i.click()
        time.sleep(2)
        # driver.save_screenshot(screens)
        # time.sleep(2)

# click outs

LinksCTA= driver.find_elements(By.XPATH,".//div[@id='custom-links']/a")
print(len(LinksCTA))


if LinksCTA is not None:
    for i in LinksCTA:
        i.click()
        driver.switch_to.window(mainpage)
        driver.switch_to.frame(1)



closeTab=driver.find_element(By.ID,"expansion-close")

closeTab.click()

time.sleep(2)

# driver.quit()






