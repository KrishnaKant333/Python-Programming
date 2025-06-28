n1 = int(input("Enter four numbers :"))
n2 = int(input())
n3 = int(input())
n4 = int(input())

if(n1>n2 and n1>n3 and n1>n4):
	print(f"The greatest of the four numbers is : {n1}")
elif(n2>n1 and n2>n3 and n2>n4):
	print(f"The greatest of the four numbers is : {n2}")
elif(n3>n1 and n3>n2 and n3>n4):
	print(f"The greatest of the four numbers is : {n3}")
elif(n4>n1 and n4>n2 and n4>n3):
	print(f"The greatest of the four numbers is : {n4}")
