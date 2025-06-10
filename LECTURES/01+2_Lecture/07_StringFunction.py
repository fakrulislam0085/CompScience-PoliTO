"""
Python provides many built-in methods to work with strings:

.upper(): Converts to uppercase.
.lower(): Converts to lowercase.
.strip(): Removes whitespace from the beginning and end.
.replace("old", "new"): Replaces a substring with another.
.find("substring"): Finds the index of a substring. *It counts space as an index too
"""

MyVarsity = "Politecnico Di Torino"
print(MyVarsity.upper())
print(MyVarsity.lower())
print(MyVarsity.replace("Torino", "Milano"))      #Replacing substring
print(MyVarsity.find("Torino"))
print(MyVarsity.strip())



name = "    Fakrul Islam   "
print(name)
print(name.strip())    #remove the spaces from the first and the last



#char conversions
x = ord('a')    #ord() func return us the unicode points of char
print(x)

y = chr(97)     #chr() func returns us the char associated with the unicode 
print(y)