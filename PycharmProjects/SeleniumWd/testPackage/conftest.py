import pytest

@pytest.fixture()
def setUp():
    print("Running demo  setup")
    yield
    print("Running demo teardown")

@pytest.fixture()
def Onetimesetup():
     print("*"* 20 + "One time modular set up " + "*"* 20)
     yield
     print("*"* 20 + "One time modular tear down " + "*"* 20)
