def goodDay(name, ending): # name and endings are arguments
	print("Have a good day",name)
	print(ending)
name = input("Enter your name : ")
goodDay(name, "Thank You")

def avg(a,b,c):
	return (a+b+c)/3 # this thing is return value
x = 5
y = 6
z = 7
average = avg(x,y,z)
print("Average =",average)
