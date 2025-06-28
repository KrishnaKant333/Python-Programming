def rem(l, word):
	for item in l:
		l.remove(word)
		return l
l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))

def strip(l, word):
	n = []
	for item in l:
		if not(item == word):
			n.append(item.strip(word))
	return n
print(strip(l, "an"))
