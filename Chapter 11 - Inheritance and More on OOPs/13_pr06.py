class Vector:
	def __init__(self, l):
		self.l = l
	def __len__(self):
		return len(self.l)

v1 = Vector([1,2,3,4,5])
print(f"This is a vector of {len(v1)} Dimensions.")
