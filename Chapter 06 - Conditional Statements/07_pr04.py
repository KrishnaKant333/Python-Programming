username = input("Enter your name : ")

if(len(username)<10):
	print(f"The given username \"{username}\" contains less than 10 characters!")
else:
	print(f"The given username \"{username}\" contains 10 or more characters!")
