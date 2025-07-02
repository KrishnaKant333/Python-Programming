class Employee:
# These @ notations are used for decorators just like staticmethod, classmethod, property, name.setter, etc.
	@property
	def name(self):
		return f"{self.fname} {self.lname}"

	@name.setter
	def name(self, value):
		self.fname = value.split(" ")[0]
		self.lname = value.split(" ")[1]

# This is also a very good example of abstraction and encapsulation i.e. how data is stored and managed is not known by the user and data is encapsulated in a packet (here, inside the class Employee)

o = Employee()
o.name = "Harry Khan"
print(o.name)
