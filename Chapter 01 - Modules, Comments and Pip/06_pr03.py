import os

# specify directory you want to list
directory_path = 'D:/VS Code/Python'

# list all files and folders in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
print(contents)
