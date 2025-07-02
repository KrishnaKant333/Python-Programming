class Complex:
	def __init__(self, r, i):
		self.r = r
		self.i = i
	def __add__(self, c2):
		return Complex(self.r + c2.r, self.i + c2.i)

	def __mul__(self, c2):
		real_part = self.r*c2.r - self.i*c2.i
		im_part = self.r*c2.i + self.i*c2.r
		return Complex(real_part, im_part)

	def __str__(self):
		sign = "+" if self.i >= 0 else "-"
		return f"{self.r} {sign} {abs(self.i)}i"

print("Enter the real and imaginary part of first complex number : ")
c1r = int(input("Real part : "))
c1i = int(input("Imaginary part : "))

c1 = Complex(c1r, c1i)
print("Enter the real and imaginary part of second complex number : ")
c2r = int(input("Real part : "))
c2i = int(input("Imaginary part : "))

c2 = Complex(c2r, c2i)
print(f"The two complex numbers are : {c1} and {c2}.")
print(f"Their sum is {c1+c2}.")
print(f"Their product is {c1*c2}.")
