def summation(n):
	if n == 1:
		return 1
	else:
		return n + summation(n-1)

num = int(input("Enter a number : "))
print(f"The sum of first {num} numbers is {summation(num)}.")
