class Demo:
	a = 4

o = Demo()
print(o.a) # Prints the class attribute becoz there is no instance attribute
o.a = 0
print(o.a) # Prints the instance attribute becoz priority
print(Demo.a) # Prints the original class attribute
# Hence the class attribute does not get changed 
