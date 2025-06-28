# print the following star pattern:
# ***
# * *
# ***

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
	if(i==1 or i==n):
		print("*"*n)
	else:
		print("*", end="")
		print(" "*(n-2), end="")
		print("*", end="")
		print("")
