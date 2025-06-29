class Employee:
	language = "Python"
	salary = 1200000

	@staticmethod # static method declaration is used so as to avoid adding self when the function is not dealing with any attributes
	def greet():
		print("Good morning")
harry = Employee()
harry.greet()
