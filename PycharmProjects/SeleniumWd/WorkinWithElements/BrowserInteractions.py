from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


class browserInteractions():
    def Test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()

        # Maximize the window

        driver.maximize_window()

        # open the url

        driver.get(baseUrl)

        # get title

        title = driver.title

        print("the title of the page is " + title)

        # get the current URl of the page

        currentUrl = driver.current_url

        #print("the url of the page is " + currentUrl)

        #driver.refresh()

        #print("the 1st refresh")

        #driver.get(driver.current_url)

        #driver.refresh()

        #print("the second refresh")

        #driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

        # driver.back()

        print("goes one step back in browser history")

        # driver.forward()

        print("goes one step forward in browser history")

        # driver.quit()
        #
        # time.sleep(3)
        #
        # login = driver.find_element_by_id("user_email")
        #
        # login.send_keys("harisrizwan@live.com")
        # abc = driver.find_element_by_id("user_password")
        # abc.send_keys("12341234")
        #
        # #method one for click
        # submit = driver.find_element_by_name("commit")
        #
        # submit.click()

        # second method to work on elements

        #driver.find_element_by_name("commit").click()

        time.sleep(3)


        #driver.find_element(By.XPATH,".//div//a[contains(text(),'Login')]").click()

        driver.find_element(By.ID,"bmwradio").click()

        #Select(driver.find_element(By.ID,"carselect")).select_by_value('benz').click()
        Select(driver.find_element(By.ID, "carselect")).



        time.sleep(3)


ff = browserInteractions()

ff.Test()
