import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "table.txt")

try:
	num = int(input("Enter a number : "))

	mul_list = [num*i for i in range(1, 11)]
	with open(file_path, "a") as f:
		f.write(f"Multiplication table of given number {num} is :\n")
		f.write(str(mul_list)+"\n")
except ValueError as e:
	print("Enter an integer only!")
	print("Error: ",e)
