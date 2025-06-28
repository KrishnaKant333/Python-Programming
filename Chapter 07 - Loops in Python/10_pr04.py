import math
num = int(input("Enter a number :"))
# prime = True
if num==0 or num==1:
	print(f"{num} is neither prime nor composite.")
elif num<0:
	print("Please enter only positive numbers!")
else:
	for i in range(2,int(math.sqrt(num))+1):
		if num%i == 0:
			# prime = False
			print(f"{num} is not a prime number")
			break
# if(prime):
# 	print(f"The number {num} is a prime number.")
# else:
# 	print(f"The number {num} is not a prime number.")
	else:
		print(f"{num} is a prime number")


'''
n = int(input("Enter a number:"))
for i in range(2, n):
	if(n%i) == 0:
		print("Number is not prime")
		break
	else:
	print("Number is prime")
'''
