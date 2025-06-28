# Recursion is a function which calls itself

def factorial(n):
	if(n==0 or n==1): # base condition (required to stop infinite loop)
		return 1
	return n*factorial(n-1)
num = int(input("Enter a number : "))
print(f"The factorial of {num} is {factorial(num)}.")
