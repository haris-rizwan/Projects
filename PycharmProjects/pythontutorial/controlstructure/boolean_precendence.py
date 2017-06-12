
"""
boolean precedence
1. not
2. and
3. or
"""

bool_output = True or not False and False

print(bool_output)

bool_output1 = (10==10 or not 10<10) and 10>10

print(bool_output1)

# it will always follow the boolean precedence , but if you want your own precedence you can use ()