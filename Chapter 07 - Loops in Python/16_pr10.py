n = int(input("Enter the number : "))
print(f"Multiplication table of {n} in reversed order is : ")
for i in range(1, 11):
	print(f"{n}X{11-i} = {n*(11-i)}")
