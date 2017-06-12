"""
continue: it will go to the start of the closest enclosing
break: it will break out of the closest enclosing loop

there is a while else condition , in which the else command will always execute when the while loop is complete
unlike in if / els situation else on excute when if is false
"""

x = 1

while x < 10:

    print("the value of x is " + str(x))

    x = x+1

    # if x == 5:
    #     break

    print("the example stops at number five")

else:
    print("end of loop")




# x = 1
#
# while x < 10:
#
#     print("the value of x is " + str(x))
#
#     x = x+1
#
#     if x == 5:
#         continue
#
#     print("the example stops at number five")