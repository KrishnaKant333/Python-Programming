l = [5,23,346,566]

# index = 0
# for item in l:
# 	print(f"The item at index {index} is {item}.")
# 	index += 1
# This same thing can be simplified with the help of enumerate function

for index, item in enumerate(l):
	print(f"The item at index {index} is {item}.")
