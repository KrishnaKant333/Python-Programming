class Employee:
	language = "Python"
	salary = 1200000

	def __init__(self, name, salary, language): # Init constructor --> This will be automatically called
		# A method which starts and ends with __ is called a dunder method
		self.name = name
		self.salary = salary
		self.language = language
		print(f"The name is {self.name}. The language is {self.language}. The salary is {self.salary}.")

	def getInfo(self):
		print(f"The language is {self.language}. The salary is {self.salary}.")

harry = Employee("Harry", 1300000, "Javascript")
harry.getInfo()
