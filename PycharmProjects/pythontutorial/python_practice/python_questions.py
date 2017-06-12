"""
Write a sample program to print a string in a specefic format
"""
#
# print("Twinkle, twinkle, little star,\
#  \n\t\tHow I wonder what you are!\
#  \n\t\t\t\tUp above the world so high, \
#  \n\t\t\t\tLike a diamond in the sky. \
#  \nTwinkle, twinkle, little star, \
#  \n\t\tHow I wonder what you are")

#write a program to print the version of python you are using
#
# import sys
#
# print(sys.version)

#write a program to print date and time
import time

# print(time.strftime("%H:%M:%S"))
#
# print(time.strftime("%I:%M:%S"))

# print(time.strftime("%d/%m/%y"))
###################################################

#area of circle program

# import math
#
#
# Radi_circle=int(input("Please enter the desired radius:"))
#
# x=Radi_circle**2*math.pi
#
# print(x)

# write a program that recives first and last name as input and prints them reverse

# F_name = input("Your First Name: ")
# L_name = input("Your Last Name: ")
#
# print(L_name + " "+ F_name)

### commaa seperated input will assign different indexes

# values = input("Input some comma seprated numbers : ")
#
# list = values.split(",")
#
# print('List : ',list)

a = int(input("Input an integer : "))
n1 = int(  a )
n2 = int("%s%s" %(a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1)
print(n2)
print(n3)








