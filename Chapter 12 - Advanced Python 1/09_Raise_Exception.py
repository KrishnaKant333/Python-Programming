a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if b == 0:
	raise ZeroDivisionError("Hey division by zero is not allowed!")
else:
	print(f"Divison a/b is {a/b}")
# Raise will actually crash the program!
