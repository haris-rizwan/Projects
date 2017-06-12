from selenium import webdriver


class FindByLink():

    def test(self):
        url= "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(url)
        elementByLinkText = driver.find_element_by_link_text("Login")


        if elementByLinkText is not None :

            print("we found an element by link text ")

        elementByPartialText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialText is not None :

            print("we found an element by partial link text")




Test = FindByLink()

Test.test()