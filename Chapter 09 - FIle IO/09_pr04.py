import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "donkey.txt")
with open(file_path, "r") as f:
	content = f.read()
contentNew = content.replace("donkey", "######")
with open(file_path, "w") as f:
	f.write(contentNew)
