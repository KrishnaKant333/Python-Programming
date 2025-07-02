class Vector:
	def __init__(self,components):
		self.components = components
	def __add__(self, other):
		result = [a + b for a, b in zip(self.components, other.components)]
		return result
# zip() takes two or more iterables (like lists, tuples, etc.) and pairs up their elements index by index.
	def __mul__(self, other):
		result = sum(a * b for a, b in zip(self.components, other.components))
		return result
	def __str__(self):
		return " + ".join(f"{val}e{i}" for i, val in enumerate(self.components))
# {val}e{i} = a generic way of writing vectors in n-dimensional space using basis notation

v1 = Vector([1,2,3,4])
v2 = Vector([4,5,6,7])

print(f"The Vectors are : {v1} and {v2}.")
print(f"Their addition is {v1+v2}")
print(f"Their dot product is {v1*v2}")
