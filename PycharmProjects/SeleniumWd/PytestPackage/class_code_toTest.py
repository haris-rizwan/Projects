# how to use test class to wrap methods under one class
# learn about autouse keywords in fixtures
# assert the result to creat a real test scenario




class ClassToTest():
    def __init__(self, value):
        self.value = value

    def sumNum(self,a,b):
        return a + b + self.value