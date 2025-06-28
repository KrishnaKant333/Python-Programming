import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "poem.txt")
with open(file_path) as f:
	if ("twinkle" in f.read() or "Twinkle" in f.read()):
		print("The file contains the word \"twinkle\"")
	else:
		print("The file does not contain the word \"twinkle\"") 
