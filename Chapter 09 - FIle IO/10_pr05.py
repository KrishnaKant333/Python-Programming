import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "donkey.txt")

words = ["donkey", "ganda", "bad"]

with open(file_path, "r") as f:
	content = f.read()
	for word in words :
		content = content.replace(word, "#"*len(word))
with open(file_path, "w") as f:
	f.write(content)
