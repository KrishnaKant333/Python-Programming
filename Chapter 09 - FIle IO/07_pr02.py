import random
import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "hiscore.txt")

def game():
	print("You are playing the game..")
	score = random.randint(1, 69)

	with open(file_path) as f :
		hiscore = f.read()
		if(hiscore != ""):
			hiscore = int(hiscore) # as f.read() reads in str so we have to convert to int for comparsion in the calculations
		else:
			hiscore = 0
		print(f"Previous High score : {hiscore}")

	print(f"Your score : {score}")
	if(score > hiscore):
		with open(file_path, "w") as f :
			f.write(str(score)) # to write into a file we must convert it to a str

game()
