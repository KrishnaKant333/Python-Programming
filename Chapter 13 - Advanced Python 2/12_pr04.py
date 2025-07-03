from functools import reduce
l = [34,54,65,56,5,34,53,43,23]

def greater(a,b):
	if a>b:
		return a
	return b

maxm = reduce(max,l)
print(maxm)
