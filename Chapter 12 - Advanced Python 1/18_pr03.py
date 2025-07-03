try:
	num = int(input("Enter a number : "))

	mul_list = [num*i for i in range(1, 11)]
	print(f"Multiplication table of given number {num} is :")
	print(mul_list)
except ValueError as e:
	print("Enter an integer only!")
	print("Error: ",e)
