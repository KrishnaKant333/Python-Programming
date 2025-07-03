from module import myFunc

# In this case, the __name__ will return the name of the file from where it is called i.e. module.py (without the extension name)

# To prevent running the code from a file we imported we can add a conditional in the source file

# After adding the conditional, the code will no longer work as its condition require it to be inside the __main__ (source) file only
