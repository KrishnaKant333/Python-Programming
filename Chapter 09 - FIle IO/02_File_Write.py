import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "myfile.txt")

st = "Hey kks you are amazing"

# f = open("myfile.txt", "w") # w for writing into a file, if the file's not there it will be created
# f.write(st) # write that string
# f.close()

with open(file_path, "w") as f: # short form of doing the above thing but more efficient and u dont have to add that f.close() at the end ^^
	f.write(st)
