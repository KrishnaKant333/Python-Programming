class Employee:
	language = "Python" # This is a class attribute
	salary = 1200000

harry = Employee()
harry.language = "Javascript" # This is an instance attribute
print(harry.language, harry.salary)
# instance attributes take preference over class attributes during assignment and retrieval

# Class attribute is the property of all objects of that class whereas Object attribute is the property of a particular object only
