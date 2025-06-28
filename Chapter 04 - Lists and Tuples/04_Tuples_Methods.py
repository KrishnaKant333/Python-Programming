a = (1,2,3,"turururu",2)
no = a.count("turururu") # counts the occurence of the given element in the tuple
print(no)
i = a.index(2) # returns the index of the first occurence of the given element in the tuple
print(i)

t1 = (1,2,3)
t2 = (4,5,6)
tc = t1 + t2 # tuple concatenation
print(tc)

tr = t1*3 # tuple can be repeated using * operator
print(tr)

print(4 in t1) # checks whether 4 is present in the tuple t1, returns boolean
print(len(t1)) # length of a given tuple
print(max(t2)) # returns the largest element in a tuple specified

sliced = tr[2:5] # tuples can be sliecd just like strings and lists
print(sliced)

p,q,r,s,t = a # tuples can be unpacked to individual variables this way
print(p,q,r,s,t)
