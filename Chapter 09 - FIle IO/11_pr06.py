import os
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "log.txt")

with open(file_path, "r") as f:
	content = f.read()

if "python" in content:
	print("\"python\" is present in the log file")
else:
	print("\"python\" is not present in the log file")
