try:
	a = int(input("Enter first number : "))
	b = int(input("Enter second number : "))

	print(f"The division {a}/{b} is {a/b}.")
except ValueError:
	print("Enter only integers!")
except ZeroDivisionError:
	print(f"The division {a}/{b} is infinite.")
