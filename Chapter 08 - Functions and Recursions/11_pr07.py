def mul_table(n):
	for i in range(1,11):
		print(f"{n}X{i} = {n*i}")

num = int(input("Enter a number : "))
print(f"The multiplication table of {num} is :")
mul_table(num)
