f = open("file.txt")
print(f.read())
f.close() # This f.close() is a burden and to get rid of it we can use the with statement

with open("file.txt") as f :
	print(f.read())

# Here we dont have to explicitly close the file 
