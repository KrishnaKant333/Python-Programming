def myFunc():
	print("Hello world!")


# __name__ will give the name of the file from which the code is executed, if it is done from the source file then it will return __main__ otherwise the name of the file.

if __name__ == "__main__":
	print("Running directly from source file : ")
	myFunc()
	print(__name__)


# Thus the code under this conditional will only work when the program is ran from the source file and not when imported

