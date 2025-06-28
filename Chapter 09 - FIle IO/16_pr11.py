import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "last.txt")
newfile_path = os.path.join(script_path, "renamed_by_python.txt")
with open(file_path) as f:
	contents = f.read()

with open(newfile_path, "w") as f:
	f.write(contents)

if os.path.exists(file_path):
	os.remove(file_path)
else:
	print("An error occurred")
