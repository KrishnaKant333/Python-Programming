username = input("Enter your name :")
date = input("Enter date :")

letter = "Dear <|name|>,\nYou are selected !\n<|Date|>"

print(letter.replace("<|name|>",username).replace("<|Date|>",date))
# chaining of replace function
