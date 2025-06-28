import os
script_path = os.path.dirname(__file__)
file1_path = os.path.join(script_path, "this.txt")
file2_path = os.path.join(script_path, "this_copy.txt")
with open(file1_path) as f:
	content1 = f.read()
with open(file2_path) as f:
	content2 = f.read()

if content1 == content2:
	print("The contents of the two files are same")
else:
	print("The contents of the two files are different")
