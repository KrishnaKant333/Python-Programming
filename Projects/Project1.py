# SNAKE WATER GUN GAME
'''
1 for snake
-1 for water
0 for gun
'''

import random
# Choice filing for system and user :
sys_num = random.choice([-1,0,1])
user_input = input("Enter your choice : ").title()

# Dictionary for abbreviations and Number Codes :
userAbb = {"S" : "Snake", "W" : "Water", "G" : "Gun"}
userDict = {"Snake" : 1, "Water" : -1, "Gun" : 0}
sysDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

# System and user's inputs' translation for printing :
sys_choice = sysDict[sys_num]
if user_input in userAbb:
	user_choice = userAbb[user_input]
else:
	user_choice = user_input

# User's input translation for calculation :
user_num = userDict[user_choice]

# Printing the choices :
print(f"Your choice : {user_choice}")
print(f"System's choice : {sys_choice}")

# Calculation for the winner :
if(sys_num == user_num):
	print("Its a draw")
else:
	if(sys_num == -1 and user_num == 1):
		print("You win!")
	elif(sys_num == -1 and user_num == 0):
		print("You lose!")
	elif(sys_num == 1 and user_num == 0):
		print("You win!")
	elif(sys_num == 1 and user_num == -1):
		print("You lose!")
	elif(sys_num == 0 and user_num == -1):
		print("You win!")
	elif(sys_num == 0 and user_num == 1):
		print("You lose!")
	else:
		print("Some error occured!!")
