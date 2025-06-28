friends = ["Apple", "orange", "titla", 54, 23.6, False]
print(friends)
friends.append("kks") # append will add an element at the end of the list
print(friends)
# to be noted that the append method makes changes to the friends list itself

l1 = [1, 5, 7, 2, -1, 2]
l1.sort() # sorts in ascending order
print(l1)
l1.reverse() # to reverse a list
print(l1)
# remember that the list is changed after using the sort method so the reverse method will act on the changed list.
l1.insert(3, "kks") # insert(index, object) to insert the object at a specified index
print(l1)
value = l1.pop(5) # the pop function has a return type so that the object deleeted will be returned
print("The object deleted from the list is :",value)
print(l1)
l1.remove("kks") # unlike pop, remove does not have a return type, it just deletes..
print(l1)
