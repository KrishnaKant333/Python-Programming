import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "newfile.txt")
with open(file_path, "w") as f:
	f.write("")
