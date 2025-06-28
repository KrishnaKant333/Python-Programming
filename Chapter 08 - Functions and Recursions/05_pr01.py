def greatest(n1,n2,n3):
	if(n1>n2):
		if(n1>n3):
			return n1
		else:
			return n3
	else:
		if(n2>n3):
			return n2
		else:
			return n3

a = int(input("Enter three numbers : "))
b = int(input())
c = int(input())

print(f"The greatest of the three numbers is : {greatest(a,b,c)}")
