import os
script_path = os.path.dirname(__file__)

def generateTable(n):
	table = f"Multiplication table of {n} is :\n"
	for i in range(1, 11):
		table += f"{n}X{i} = {n*i}\n"
		file_path = os.path.join(script_path, f"tables/table_{n}.txt")

	with open(file_path, "w") as f:
		f.write(table)

for i in range(2, 21):
	generateTable(i)
