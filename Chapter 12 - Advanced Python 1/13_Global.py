a = 89 # This is global variable a

def funk():
	global a # This declaration is used to change the value of a global variable from a function
	a = 3 # This is local variable a
	print(a)

funk()
print(a) # This will print global a
