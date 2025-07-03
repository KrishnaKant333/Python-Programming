a = "{} is a good {}".format("harry", "boy")
# same as :
a = "{0} is a good {1}".format("harry", "boy")
print(a)

# This is format command which was previously used much but now is inferior to f string.
b = "{1} is a good {0}".format("harry", "boy")
print(b)
