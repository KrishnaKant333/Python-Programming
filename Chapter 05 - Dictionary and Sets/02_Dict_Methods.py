marks = {
	"harry": 85,
	"kks": 90,
	"dv": 100,
	0 : "harry"
}
print(marks)
print(len(marks)) # will return the length i.e. the number of key-value pairs in the dictionary
print(marks.items()) # get items of the dictionary in the form of tuples
print(marks.keys()) # get the keys(left hand side elements) of the dictionary
print(marks.values()) # get the values(right hand side elements) of the dictionary
marks.update({"kks":85, "turururu":99})
# update() updates the values of a key if present and if not then adds that particular key value pair to the dictionary
print(marks)

print(marks.get("kks")) # the get() method is used to return the value at the key entered, if the key is not present it returns none
print(marks["kks"]) # marks[] method also returns the value at the key entered but if the key is not present it throws an error
print(marks.get("yash")) # --> returns None
# print(marks["yash"]) # --> throws an error
value1 = marks.pop("turururu", "default")
print(value1)
value2 = marks.pop("tururur", "default")# pop removes the specified key and returns the corresponding value, if key is not present then it will return "default", if default is also not provided it will throw KeyError
print(value2)
print(marks)
marks.clear() # clears the dictionary
print(marks)
