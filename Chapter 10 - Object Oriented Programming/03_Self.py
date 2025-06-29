class Employee:
	language = "Py"
	salary = 1200000

	def getInfo(self):
		print(f"The language is {self.language}. The salary is {self.salary}")
	def greet(self):
		print("Good Morning")

harry = Employee()
harry.language = "Javascript"
harry.greet()
harry.getInfo()
# harry.getInfo() is the equivalent of Employee.getInfo(harry)
# That's why its throwing an error as getInfo does not take in an argument in its definition but the function call tries to send it
# For this we give the function an argument usually named Self
