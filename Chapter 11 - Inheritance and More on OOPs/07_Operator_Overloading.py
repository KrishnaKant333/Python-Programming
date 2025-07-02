# Operators in python can be overloaded using dunder methods. These methods are called when a given operator is used on the objects. Operators in python can be overloaded using the following methods for eg:
# __add__, __sub__, __mul__, __truediv__, __floordiv__, __str__(), __len__()

class Number:
	def __init__(self, n):
		self.n = n
	def __add__(self, num):
		return self.n + num.n
n = Number(1)
m = Number(2)

print(n+m)
