def goodDay(name, ending="Thank You"):
	print("Have a good day",name)
	print(ending)
name = input("Enter your name : ")
goodDay(name) # even if we dont supply an "ending" argument then also the code will work without throwing error as a default ending argument is set
goodDay(name, "LOL") # here the ending argument is provided as LOL so it will overwrite the default one
