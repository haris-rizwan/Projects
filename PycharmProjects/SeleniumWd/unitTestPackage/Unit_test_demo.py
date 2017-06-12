import unittest

class TestCaseDemo(unittest.TestCase):

#@classmethod is an annotator in python which is used we call them decorators in python .
#we need them to define it is a class level method
    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("Run only once before all Tests")
        print("#" * 30)

    def setUp(self):
        print("Run before every test")
        #it is a pre test set up it will set up everything from initiating a webdriver
        # to load a test url or any other requirements that are required for testing
    def test_methodA(self):
        print("Run test A")

    def test_methodB(self):
        print("Run test B")

    def tearDown(self):
        print("Run after every test")


    @classmethod
    def tearDownClass(cls):
       print("#" * 30)
       print("Run only once after all Tests")
       print("#" * 30)

if __name__ == "__main__":
    unittest.main(verbosity=2)





