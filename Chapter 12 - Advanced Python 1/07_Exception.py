try:
	a = int(input("Enter a number : "))
	print(a)
except Exception as e:
	print(e)

print("Thank you")

# If we enter a string for example instead of a number then :
# without try except block the program would have crashed there and any code below it would not have been executed.
# But with try except block the program will not throw an error but will be prepared if a error like this comes, then we may simply print the error and continue with the code below!
