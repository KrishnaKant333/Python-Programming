import math

class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n**2}.")
    def cube(self):
        print(f"The cube of {self.n} is {self.n**3}.")
    def sqrt(self):
        if self.n >= 0:
            print(f"The square root of {self.n} is {math.sqrt(self.n)}")
        else:
            print("The square root of negative numbers is not defined!")


while True:
    num = float(input("Enter a number: "))
    Calci = Calculator(num)

    print("1 For Finding the Square")
    print("2 For Finding the Cube")
    print("3 For Finding the Square Root")
    print("0 For Exiting the program")

    prompt = int(input("Enter the operation you'd like to perform: "))

    if prompt == 1:
        Calci.square()
    elif prompt == 2:
        Calci.cube()
    elif prompt == 3:
        Calci.sqrt()
    elif prompt == 0:
        exit()
    else:
        print("Please select a valid choice only!")
