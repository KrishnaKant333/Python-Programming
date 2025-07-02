class TwoDVector:
	def __init__(self, i, j):
		self.i = i
		self.j = j

	def __str__(self):
		return f"The two dimensional vector is : {self.i}i + {self.j}j"
class ThreeDVector(TwoDVector):
	def __init__(self, i, j, k):
		super().__init__(i, j)
		self.k = k

	def __str__(self):
		return f"The three dimensional vector is : {self.i}i + {self.j}j + {self.k}k"

print("Enter the x and y components of the vector : ")
x = int(input())
y = int(input())
a = TwoDVector(x, y)
print(a)

isz = input("Is there a z component of the vector ? (Yes/No) ")
if isz.lower() == "yes":
	z = int(input("Enter the z component of the vector : "))
	b = ThreeDVector(x, y, z)
	print(b)
else:
	print("Alright!")
