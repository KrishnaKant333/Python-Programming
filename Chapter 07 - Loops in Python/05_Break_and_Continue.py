print("Iteration 1 :")
for i in range(100):
	if(i==34):
		break # to exit the loop abruptly when i = 34
	print(i)

print("Iteration 2 :")
for i in range(100):
	if(i==34):
		continue # skip the iteration when i = 34 and then continue after it
	print(i)
