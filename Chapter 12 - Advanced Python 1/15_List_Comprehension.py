myList = [1,2,5,6,9]

# squaredList = []
# for item in myList:
# 	squaredList.append(item*item)

# we can simplify this using list comprehension

squaredList = [item*item for item in myList]

print(squaredList)
