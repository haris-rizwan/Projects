from selenium import webdriver

from selenium.webdriver.common.by import By


class FindingElements():

    def test(self):
        url= "https://www.airbnb.ca/?af=43720035&c=A_TC%3Drqnexjh8ka%26G_MT%3De%26G_CR%3D94236318404%26G_N%3Dg%26G_K%3Dairbnb%27%26G_P%3D%26G_D%3Dc&atlastest5=true&gclid=CPfboZD4i9MCFca2wAodZIIL4A"
        driver = webdriver.Firefox()
        driver.get(url)
        elementById = driver.find_elements_by_class_name("inputs")

        Length1 = len(elementByClass)


        if elementById is not None :

            print("Number of elements with Class name inputs is " +  str(Length1))

        elementByTag = driver.find_elements(By.TAG_NAME,"div")



        Length2 = len(elementByTag)

        if elementByTag is not None :

            print("Number of elements with tag div is  "  +  str(Length2))




Test = FindingElements()

Test.test()