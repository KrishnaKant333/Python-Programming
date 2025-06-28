# Print the following star pattern :
#   *
#  ***
# ***** For n = 3

n = int(input("Enter the value of n : "))

for i in range(1, n+1):
	print(" "*(n-i), end="") # end="" means end with the thing inside the double quotes so that the new line wont be present becoz of the print() statement
	print("*"*(2*i-1), end="")
	print("")
