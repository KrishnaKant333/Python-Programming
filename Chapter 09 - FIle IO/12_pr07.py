import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "log.txt")

with open(file_path, "r") as f:
	lines = f.readlines()

lineno = 1
for line in lines:
	if "python" in line:
		print(f"\"python\" is present in the log file. Line no.: {lineno}")
		break
	lineno += 1
else:
	print("\"python\" is not present in the log file")
