username = input("Enter your name:")
check = username.find("  ")
print(f"The index where double space is present in your entered name \"{username}\" is ", check)
print(f"The String when the double space is replaced with single space is", username.replace("  "," "))
