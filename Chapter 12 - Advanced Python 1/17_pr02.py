l = [4,56,3,134,54,65,3,435]

# WAP to print the 3rd, 5th, 7th element of the list using enumerate function

for index, item in enumerate(l):
	if index in [2,4,6]:
		print(item)
