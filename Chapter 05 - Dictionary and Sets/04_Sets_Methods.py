s = {1, 5, 32, 5, 5, 5, 67, "harry"}
s.add(566) # adds an element to the set
print(s)
print(len(s)) # returns the length of the set
s.remove(5) # removes the element 5 from the set
print(s)
s.pop() # removes a random element from the set --> not ideal to be used quite often
print(s)
s.clear() # clears the set
print(s) # will print an empty set i.e. set()

s1 = {1, 2, 4, 5}
s2 = {5, 6, 9}
print(s1.union(s2)) # set union operation --> returns a set with values from both the sets

print(s1.intersection(s2)) # set intersection operation --> returns a set with only those values which are common in both the sets
# Set difference operator :
print(s1-s2) # returns a set with values present in s1 but not in s2
print(s2-s1) # returns a set with values present in s2 but not in s1

print(s1.issuperset({1,2})) # whether s1 is the superset of {1,2} or not --> returns boolean
print({5,6,10}.issubset(s2)) # whether {5,6,10} is subset of s2 or not --> returns boolean
