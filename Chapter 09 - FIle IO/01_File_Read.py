import os
script_dir = os.path.dirname(__file__)  # This file's folder
file_path = os.path.join(script_dir, "file.txt")  # Full path to file.txt
f = open(file_path) # open a file to work with (by default it is set to be opened in (rt) read in text mode)
data = f.read() # read the contents of the file
print(data)
f.close() # make sure to close the file once we are done working with it
