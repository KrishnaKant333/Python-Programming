try:
	a = int(input("Enter first number : "))
	b = int(input("Enter second number : "))
	print(a/b)
except ZeroDivisionError as z:
	print("Divisor found to be zero!")
	print("Error:",z)
except ValueError as v:
	print("Please enter a number only!")
	print("Error:",v)
except Exception as e:
	print(e)
