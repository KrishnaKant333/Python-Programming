class Programmer:
	company = "Microsoft"
	def __init__(self, name, salary, pin):
		self.name = name
		self.salary = salary
		self.pin = pin
# P = Programmer("Harry", 1200000, 245001)
# print(P.name, P.company, P.pin, P.salary)
name = input("Enter your name: ")
salary = input("Enter your salary: ")
pin = input("Enter your pin: ")
P = Programmer(name, salary, pin)
print("Your info are : ")
print(f"\tName : {P.name}\n\tSalary : {P.salary}\n\tPin : {P.pin}\n\tCompany : {P.company}")
