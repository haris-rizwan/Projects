"""
boolean operators
*****************

AND
-------------------------
True and True = true
True and false = false
false and false = false

------------------------

 or
-----------------------
True and True  = true
true and false = true
false and false = false

-------------------------

not

----------------------

not true = false
not false = true

"""



and_output1 = (250==250) and (300>250)

and_output2 = (250==250) and (300>400)

and_output3 = (250!=250) and (300>250)

print(and_output3)

or_output1 = (25>24) or (24==24)

or_output2 = (25>24) or (24==35)

or_output3 = (24>24) or (35>45)

print(or_output3)

not_output1 = not (25==25)

not_output2 = not (756>756)

print(not_output2)