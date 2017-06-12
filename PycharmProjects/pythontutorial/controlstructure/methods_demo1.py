"""
methods is function that we can create in python and reuse it multiple times in our code

methods make the job eaisier so that there is no repetition of code
it is defined by def

methods or function will always return one value

the return value in function save the answer after runing the method
"""

def addition(n1,n2):
    """
    this comment box is tp define the method or function
    :param n1:
    :param n2:
    :return:
    """
    print(n1+n2)

def multiplication(n1,n2):
    print(n1*n2)


addition(20,40)

multiplication(2,20)

# the return value in function save the answer after runing the method

def mul(n1,n2):
    return n1 * n2
#return saves the value then you have to assign a variable to that value to use it however you want
value= mul(2,3)

print(value)

def metorcities(city):
    l =["montreal","toronto","halifax"]

    if city in l:
        return True
    else:
        return False


city=metorcities("montreal")

print(city)

