import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "myfile.txt")

st = input("Enter your string : ")

with open(file_path, "a") as f: # in append mode the string will just be added at the end of the file instead of overwriting the file
	f.write("\n"+st)
