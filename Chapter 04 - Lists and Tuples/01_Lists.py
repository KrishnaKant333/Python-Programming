# lists are containers to store a set of values of any data type
# lists are indexed just like  strings and slicing of lists works just the same as strings
friends = ["Apple", "orange", "titli", 54, 23.6, False]
print(type(friends))
print(friends[1:5])
# unlike strings, lists can be changed i.e. they are mutable and fully flexible
friends[2] = "titla"
print(friends)
