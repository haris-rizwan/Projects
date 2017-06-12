from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import os


baseUrl = "https://srv1.contobox.com/v3/preview.php?id=14636"
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get(baseUrl)
# time.sleep(5)
driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(baseUrl)

#it will first go to the pre banner expansion iframe a
frame1 = driver.find_element(By.TAG_NAME,"iframe")
value=frame1.get_attribute("id")
driver.switch_to.frame(value)
print(value)

# after that it will go find the element of pre banner and click it
banner=driver.find_element(By.ID,"cb-ctr")
banner.click()
time.sleep(4)

#now again we have to make it switch to the expanded banner main
driver.switch_to.default_content()
driver.switch_to.frame(1)

#we store the main expanded banner handle in the mainpage
mainpage=driver.current_window_handle

tab2=driver.find_element(By.ID,"component-button-1")
tab2.click()

tab3=driver.find_element(By.CLASS_NAME,"applyNow")
tab3.click()

driver.switch_to.window(mainpage)
driver.switch_to.frame(1)

time.sleep(3)
tab4=driver.find_element(By.ID,"component-button-2")
tab4.click()

#social buttons
SocialButtons = driver.find_elements(By.CLASS_NAME,"social-button")

print(len(SocialButtons))

if SocialButtons is not None:
    for i in SocialButtons:
        i.click()
        driver.switch_to.window(mainpage)
        driver.switch_to.frame(1)

closeTab=driver.find_element(By.ID,"expansion-close")

closeTab.click()

time.sleep(2)

driver.quit()





