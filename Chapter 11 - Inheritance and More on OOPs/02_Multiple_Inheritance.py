class Employee: # Base Class 1
	company = "ITC"
	name = "Default Name"
	salary = 3628800
	def show(self):
		print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Coder: # Base Class 2
	language = "Python"
	def printLanguages(self):
		print(f"Out of all the languages here is your language : {self.language}")

class Programmer(Employee, Coder): # Child Class inherited from both Employee and Coder base classes
	company = "ITC Infotech"
	def showLanguage(self):
		print(f"The language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
print(a.company, b.company)
