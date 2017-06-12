import pytest

from PytestPackage.class_code_toTest import ClassToTest

@pytest.mark.usefixtures("OnetimesetUp","setUp")
class TestClassDemo():


    @pytest.fixture(autouse=True)
    #it creates a fixture and the instance/object created in the method is accessible to all the methods
    # if ou want to use the return value you have to define it in the method
    def ClassSetup(self,OnetimesetUp):
        # if you want to use the return value from conftest in your test methods
        #you have to define the fixture as a parameter of the class.
        self.giveNumber = ClassToTest(self.value)

    def test_methodA(self):
        result = self.giveNumber.sumNum(2,8)
        assert result == 10
        print("Running method A")

    def test_methodB(self):
        print("Running method B")
