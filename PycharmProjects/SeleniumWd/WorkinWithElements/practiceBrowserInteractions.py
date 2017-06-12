from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class practice():
    def __init__(self):
        baseUrl = "https://www.airbnb.com/?af=43888734&c=brdsearch_d_engus_na_na_p2_txt"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.get(baseUrl)

    def elementclick(self,locator,locatortype):
        if locatortype == "id":
            self.driver.find_element(By.ID,locator).click()
        elif locatortype == "xpath":
            self.driver.find_element(By.XPATH, locator).click()
        else:
            self.driver.find_element(By.NAME, locator).click()


    def enterCityName(self, usercity):
        _city_name = "GeocompleteController-via-SearchBarLarge"
        city = self.driver.find_element(By.ID,_city_name)
        city.clear()
        city.send_keys(usercity)
        time.sleep(2)
        self.driver.find_element(By.ID, "GeocompleteController-via-SearchBarLarge").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        self.driver.find_element(By.ID, "GeocompleteController-via-SearchBarLarge").send_keys(Keys.ENTER)

    def selectCheckInDate(self, checkindate):
        _check_in_date = ".//*[@id='site-content']//button[contains(@aria-label,' " + checkindate + "')]"
        InDate = self.driver.find_element(By.XPATH,_check_in_date)
        InDate.click()

    def selectCheckOutDate(self, checkoutdate):
        _check_out_date = ".//*[@id='site-content']//button[contains(@aria-label,'" + checkoutdate + "')]"
        OutDate = self.driver.find_element(By.XPATH, _check_out_date)
        OutDate.click()

    def closemodalpanel(self):
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "modal-close").click()

    def selectGuests(self):
        time.sleep(2)
        _guest_button = ".//*[@id='site-content']/div/div/div[1]//button[@data-reactid='182']"
        _adult_button = ".//*[@id='site-content']//button[@aria-label='add']"
        guest = self.driver.find_element(By.XPATH,_guest_button)
        guest.click()
        time.sleep(2)
        adult = self.driver.find_elements(By.XPATH,_adult_button)
        for i in adult:
            i.click()
        # adult = self.driver.find_elements(By.XPATH, _adult_button)
        # for i in range(0, len(adult)):
        #     adult[i].click()

    def clickApply(self):
        _apply_button = "component_9w5i1l-o_O-component_button_r8o91c"
        wait = WebDriverWait(self.driver, 5)
        applyButton = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, _apply_button)))
        applyButton.click()

    def Test(self):
        self.enterCityName("New York")
        self.selectCheckInDate("30 April 2017")
        self.selectCheckOutDate("25 May 2017")
        # self.closemodalpanel()
        self.selectGuests()
        self.clickApply()

ff = practice()
ff.Test()


