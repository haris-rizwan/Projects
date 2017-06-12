from selenium import webdriver


class FindingElementIdName():

    def test(self):
        url= "https://www.airbnb.ca/?af=43720035&c=A_TC%3Drqnexjh8ka%26G_MT%3De%26G_CR%3D94236318404%26G_N%3Dg%26G_K%3Dairbnb%27%26G_P%3D%26G_D%3Dc&atlastest5=true&gclid=CPfboZD4i9MCFca2wAodZIIL4A"
        driver = webdriver.Firefox()
        driver.get(url)
        elementById = driver.find_element_by_id("GuestPickerTrigger__button")


        if elementById is not None :

            print("we found an element by ID ")

        #elementByName = driver.find_element_by_name("show-hide")

        #if elementByName is not None :

           # print("we found an element by Name")




Test = FindingElementIdName()

Test.test()