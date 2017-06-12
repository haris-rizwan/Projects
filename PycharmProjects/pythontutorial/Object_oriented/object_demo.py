"""
object oriented programming
# """
#
#
# class car(object):
#
#     def __init__(self, make,model,year,):
#
#         self.make = make
#
# # __init__ command is like the constructe in python language
# c1 = car("honda")
#
# print(c1.make)
#
class product(object):



    def __init__(self,name,quantity,color):

        self.name = name
        self.quantity = quantity
        self.color = color



    def getQuantity(self):

        return (self.quantity)

    def add(self,num):

       self.quantity=self.quantity + num







p1 = product("shampoo",20,"yellow")

p2 = product("salt",10,"white")




# p1.add(40)
#
# print(p1.getQuantity())
#
# p1.add(60)
#
# print(p1.getQuantity())






