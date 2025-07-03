# Finally block executes no matter what

# in a scenario like this, finally can be neglected :
# try:
# 	a = int(input("Enter a number : "))
# 	print(a)
# except Exception as e:
# 	print(e)
# finally:
# 	print("Thank you for using our program!")

# but if we're under a function that returns after try and except blocks then also finally will run :
def func():
	try:
		a = int(input("Enter a number : "))
		print(a)
		return
	except Exception as e:
		print(e)
		return
	finally:
		print("Thank you for using our program!")
func()
