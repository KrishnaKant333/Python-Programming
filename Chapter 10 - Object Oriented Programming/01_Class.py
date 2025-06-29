class Employee:
	lng = "py" # This is a class attribute
	salary = 1200000

harry = Employee()
harry.name = "harry" # This is an instance/object attribute
print(harry.name, harry.lng, harry.salary)
rohan = Employee()
rohan.name = "rohan roro robinson"
print(rohan.name, rohan.salary, rohan.lng)

# here name is instance/object attribute and salary and language are class attributes as they directly belong to the class
