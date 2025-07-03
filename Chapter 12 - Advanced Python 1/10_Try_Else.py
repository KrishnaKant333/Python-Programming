try:
	a = int(input("Enter a number : "))
	print(a)
except Exception as e:
	print(e)
else:
	print("Thank you for using our program!")

# Try with else Logic :
# if try executes then else will also execute , and if exception is thrown then only except block will execute

# Alternatively saying, else will run to prove that try was successful
