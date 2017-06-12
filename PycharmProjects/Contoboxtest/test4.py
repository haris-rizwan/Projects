from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import os
from selenium.common.exceptions import *


baseUrl = "https://srv1.contobox.com/v3/preview.php?id=14517"

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

time.sleep(3)


tab = driver.find_elements(By.CSS_SELECTOR,".tab-title")
print(len(tab))

# clickelement = driver.find_element(By.XPATH,".//*[@id='component-button-1']")
#
# clickelement.click()

if tab is not None:
    for i in tab:
        i.click()


        # driver.save_screenshot(screens)
        # time.sleep(2)

# wait = WebDriverWait(driver, 10, poll_frequency=1,
#                              ignored_exceptions=[NoSuchElementException,
#                                                  ElementNotVisibleException,
#                                                  ElementNotSelectableException])

LinksCTA= driver.find_elements(By.XPATH,".//div[@id='custom-links']/a")
print(len(LinksCTA))



# print(len(LinksCTA))


if LinksCTA is not None:
    for i in LinksCTA:
            if i.is_displayed():
                i.click()
            else:
                print("Element no optically visible")

    driver.switch_to.window(mainpage)
    driver.switch_to.frame(1)





time.sleep(4)

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






