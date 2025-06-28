name1 = "Krishnakant"
print(name1)
print("The length of the 'name' string is :",len(name1))

print("Does the 'name' string ends with 'ankant' pattern : ",name1.endswith("ankant"))
print("Does the 'name' string starts with 'Krish' pattern : ",name1.startswith("Krish"))
# these two are case sensitive

name2 = "krishnakant"
print(name2.capitalize()) # capitalizes the first character of the first word in the string, only!
print(name2.count("k")) # counts the total occurence of the given character
print(name2.find("h")) # returns the index of the first occurence of the given character from the string
# find() can take in a character as well as a whole word/string

name3 = "Krishnakant Sharma"
print(name3.find("Sharma"))

name4 = "Hacker Krishnakant Sharma is a Hacker"
print(name4.replace("Hacker","Programmer")) # replace() replaces all occurences of a word in a string

name5 = "krishnakant sharma"
print(name5.title()) # capitalizes the first character of all the words in the string, only!
print(name5.upper()) # upper case all characters in name5 string
name6 = "KRISHNAKANT SHARMA"
print(name6.lower()) # lower case all characters in name6 string
name7 = "      krishna   kant sharma        "
print(name7.strip()) # removes leading and trailing whitespaces
# for only leading or only trailing whitespaces use lstrip() and rstrip() resp
print(name7.lstrip())
print(name7.rstrip())
print(name7.split())


# even after all these operations on a string, a string is immutable i.e. it cannot be changed no matter what, all these functions just return a new string modified from the original string
