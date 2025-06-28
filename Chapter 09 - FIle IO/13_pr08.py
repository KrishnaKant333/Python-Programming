import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "this.txt")
file2_path = os.path.join(script_path, "this_copy.txt")

with open(file_path) as f: 
	contents = f.read()

with open(file2_path, "w") as f:
	f.write(contents)
