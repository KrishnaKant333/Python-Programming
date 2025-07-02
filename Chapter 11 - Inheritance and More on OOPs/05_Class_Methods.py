class Employee:
	a = 1

	@classmethod # A method which is bound to the class but not its object and so the instance attribute will not be prioritized in Class methods
	def show(cls):
		print(f"The class attribute of a is {cls.a}.")

o = Employee()
o.a = 45
o.show()
