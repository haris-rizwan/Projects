from selenium import webdriver


class FindingXpathCss():

    def test(self):
        url= "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)
        elementByXpath = driver.find_element_by_xpath(".//*[@id='openwindow']")


        if elementByXpath is not None :

            print("we found an element by Xpath ")

        elementByCss = driver.find_element_by_css_selector(".left-align>fieldset>legend")

        if elementByCss is not None :

            print("we found an element by Css")




Test = FindingXpathCss()

Test.test()