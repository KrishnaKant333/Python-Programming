name = "harry"
#       01234
# indexing starts from 0 from beginning and -1 from ending

# positive slicing :
short1 = name[0:3] # slice name string from index 0 to 3 excluding 3 i.e. first 3 letters of name string
print(short1)

character1 = name[1] # get character at index 1 from name
print("The character at index 1 in name string is :",character1)

# negative slicing :
short2 = name[-4:-1] # slice name string from index -4 i.e. a to index -1 excluding -1
print(short2)
# name[-4,-1] is same as name[1,4]

# other adv slicing :
name1 = name[:4] # if first number's place is empty it means 0th index
print(name1)

name2 = name[2:] # if last number's place is empty it means string length
print(name2)

# slicing with skips :
name3 = name[0:4:2] # get characters from 0 to 4 but skip 2 characters after each character withdrawn
print(name3)
# harry 0 to 4 means harr but skipping 2 characters so after h we skip a and r and get r
# 01234

# even after all these operations on a string, a string is immutable i.e. it cannot be changed no matter what, all these functions just return a new string modified from the original string
