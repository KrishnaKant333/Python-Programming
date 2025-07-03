l = [1,2,3,4,5]
def even(n) -> bool:
	if n%2 == 0:
		return True
	return False
evenList = filter(even, l)
print(list(evenList))
