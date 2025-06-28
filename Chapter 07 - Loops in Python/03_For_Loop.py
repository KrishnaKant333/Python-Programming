for i in range(4): # range(4) is understood as range(0,4)
	print(i)

print("Step size 4 in range from 0 to 100 looks like : ")
for j in range(0, 100, 4): # range(1, 100, 4) means print from 1 to 100 with jump of 4
	print(j)

print("Printing a list, tuple or strings(iterables) :")
l = [1, "harry", 'kks', 'dv', 78.6]
for i in l:
	print(i)
s = "Harry"
for i in s:
	print(i)
