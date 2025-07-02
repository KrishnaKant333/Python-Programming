class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
	def __mul__(self, other):
		return (self.x * other.x + self.y * other.y + self.z * other.z)
	def __str__(self):
		return f"{self.x}i + {self.y}j + {self.z}k"


v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

print(f"The Vectors are : {v1} and {v2}.")
print(f"Their addition is {v1+v2}")
print(f"Their dot product is {v1*v2}")
