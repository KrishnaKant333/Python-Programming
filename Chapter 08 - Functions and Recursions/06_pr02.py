# My first logic :

# def convertor(i_scale, o_scale, t):
# 	if(i_scale == "celsius" or i_scale == "c"):
# 		if(o_scale == "fahrenheit" or o_scale == "f"):
# 			f = 9*t/5 + 32
# 			return f
# 		if(o_scale == "kelvin" or o_scale == "k"):
# 			k = t - 273.15
# 			return k

# 	if(i_scale == "fahrenheit" or i_scale == "f"):
# 		if(o_scale == "celsius" or o_scale == "c"):
# 			c = 5*(t-32)/9
# 			return c
# 		if(o_scale == "kelvin" or o_scale == "k"):
# 			k = 5*(t-32)/9 - 273.15
# 			return k

# 	if(i_scale == "kelvin" or i_scale == "k"):
# 		if(o_scale == "fahrenheit" or o_scale == "f"):
# 			f = 9*(t+273.15)/5 + 32
# 			return f
# 		if(o_scale == "celsius" or o_scale == "c"):
# 			c = t + 273.15
# 			return c

# Monday's logic :

def to_celsius(t, scale):
	if scale in ["c", "celsius"]:
		return t
	if scale in ["f", "fahrenheit"]:
		return (t-32)*5/9
	if scale in ["k", "kelvin"]:
		return t - 273.15

def from_celsius(t, scale):
	if scale in ["c", "celsius"]:
		return t
	if scale in ["f", "fahrenheit"]:
		return (t*9/5) + 32
	if scale in ["k", "kelvin"]:
		return t + 273.15

def converter(i_scale, o_scale, t):
	celsius_temp = to_celsius(t, i_scale)
	return from_celsius(celsius_temp, o_scale)

input_scale = input("Which scale would you like to enter the temperature in ?\n").lower()
output_scale = input("Which scale would you like to convert it to ?\n").lower()
temp = float(input("Enter the temperature : "))
print(f"Temperature entered is \"{temp}\" in \"{input_scale}\" scale.")
converted = converter(input_scale, output_scale, temp)
print(f"Required temperature in \"{output_scale}\" scale is \"{converted}\"")
