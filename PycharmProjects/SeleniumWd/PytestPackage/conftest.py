import pytest

@pytest.fixture()
def setUp():
    print("Running demo  setup")
    yield
    print("Running demo teardown")

# test module is a a test.py file
@pytest.fixture(scope="class")
def OnetimesetUp(request,browser,baseurl):
    if browser == "firefox":
        value = 10
        print("Run test on ff")
    elif browser == "chrome":
        value = 10
        print("Run test on chrome")

    else:
        value = 0
        print("opera")

    print("*"* 20 + "One time modular set up " + "*"* 20)

    if request.cls is not None:
        # if the class value is not none then return the value from one time setup to
        # to the test class
          request.cls.value = value
    yield value
    print("*"* 20 + "One time modular tear down " + "*"* 20)

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--OStype")
    parser.addoption("--baseurl")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def baseurl(request):
    return request.config.getoption("--baseurl")