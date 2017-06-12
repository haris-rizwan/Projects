import pytest

from PytestPackage.class_code_toTest import ClassToTest

@pytest.mark.usefixtures("OnetimesetUp","setUp")
class TestClassDemo():


    @pytest.fixture(autouse=True)
    #it creates a fixture and it is accessible to all the methods you do not have-
    # -to call the fixture method in every method
    def ClassSetup(self):
        self.giveNumber = ClassToTest(10)

    def test_methodA(self):
        result = self.giveNumber.sumNum(2,8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.giveNumber.sumNum(9,1)
        assert result == 20
        print("Running method B")
