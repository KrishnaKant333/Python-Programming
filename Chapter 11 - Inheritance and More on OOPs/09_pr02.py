class Animal:
	pass
class Pet(Animal):
	pass
class Dog(Pet):
	@staticmethod
	def bark():
		print("Bhau bhau!")
d = Dog()
d.bark()
