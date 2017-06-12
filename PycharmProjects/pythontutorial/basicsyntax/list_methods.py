# in built methods for lists
# they are most similar like the string methods like indexing


roommates = ["haris","umair","sumair"]

print(roommates)

roommates.append("waleed")

print(roommates)

# append will add objects in the list but it will always add the object at the end of the list

len(roommates)
lenght = len(roommates)

print(lenght)


roommates.insert(1,"moiz")

print(roommates)

# by using insert command we can add values at the desired

# pop creates a seperate memory space for the object that is removed

#y = roommates.pop(2)

#print(y)

#print(roommates)
# .remove command deletes the value permenantly 
roommates.remove("waleed")

print(roommates)

cars = ["honda","mercedez","fiat","nissan","bmw"]

print(cars)

cars.sort()

print(cars)