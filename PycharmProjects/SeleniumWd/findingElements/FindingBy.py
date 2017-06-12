from selenium import webdriver

from selenium.webdriver.common.by import By


class FindingBy():

    def test(self):
        url= "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)
        elementById = driver.find_element(By.ID,"carselect")


        if elementById is not None :

            print("we found an element by Id")

        elementByXpath = driver.find_element(By.XPATH,"//button[@id='openwindow']")

        if elementByXpath is not None :

            print("we found an element by Css")




Test = FindingBy()

Test.test()