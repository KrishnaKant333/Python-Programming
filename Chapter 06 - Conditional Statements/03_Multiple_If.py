a = int(input("Enter a number :"))

# Multiple If Statements are independent of each other and will run if the condition is true irrespective of other if statements

# If statement no. 1
if(a%2==0):
	print(f"{a} is even")
# End of if statement no. 1

# If statement no. 2
if(a>49):
	print("The number entered is greater than 49")
elif(a>99):
	print("The number entered is greater than 99")
else:
	print(f"You have entered {a}")
# End of if statement no. 1
