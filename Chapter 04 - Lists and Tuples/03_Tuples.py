# Tuples are like lists but they, unlike lists, are immutable
a = (1,2,3,"turururu")
print(a)
print(type(a))
b = () # emtpy tuple
print(type(b))
c = (1) # this does not count as a tuple rather an integer
print(type(c))
d = (1,) # this is a tuple containing only 1 element
print(type(d))
