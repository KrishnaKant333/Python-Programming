class Employee: # Parent Class or Base Class
	company = "ITC"
	def show(self):
		print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee): # Child Class or Derived Class
	company = "ITC Infotech" # The same property of the base class can be overwritten in inherited class
	def showLanguage(self):
		print(f"The language is {self.language}")

a = Employee()
b = Programmer()
print(a.company, b.company)
