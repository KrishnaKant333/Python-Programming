import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "file.txt")
with open(file_path, "r") as f:

# to get all the lines in the form of a list : readlines() function
	# lines = f.readlines()
	# print(lines, type(lines))

# to get each line individually in the form of a string : readline() function
	# line1 = f.readline()
	# print(line1, type(line1))
	# line2 = f.readline()
	# print(line2, type(line2))
	# line3 = f.readline()
	# print(line3, type(line3))


# Use a while loop to do the same for every line out there in the file as we dont know
	line = f.readline()
	while(line != ""):
		print(line, end="")
		line = f.readline()
