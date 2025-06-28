# Set is a collection of non repetative elements

# 1. Sets are unordered
# 2. Sets are unindexed
# 3. There is no way to change items in a set
# 4. Sets cannot contain duplicate values

s = {1, 5, 32}
s1 = {} # this is a empty dictionary not a set
print(type(s1))
# to make a empty set :
e = set()
print(type(e))

# only first occurence of an element in a set is considered, even if there are more than occurences of the same element :
s2 = {1, 5, 32, 5, 5, 5, 67, "harry"}
print(s2) # note that order is not maintained in a set
