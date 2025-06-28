age = int(input("Enter your age :"))
# If elif else ladder
if(age>120):
	print("Please Enter valid age only!")
elif(age>=18):
	print("You are above the age of consent")
	print("Good for you")
	# to remain inside the if statement we can continue using code with the indentation otherwise it will be considered outside of if statement
elif(age<=0):
	print("Please Enter valid age only!")
elif(age<18):
	print("You are below the age of consent")
