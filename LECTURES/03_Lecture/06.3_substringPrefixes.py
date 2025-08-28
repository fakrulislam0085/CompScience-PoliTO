'''
This program takes a file name as input and tells us what types of file it is.
In this program, we have used ".startswith(" ")" function to determine the last substring of our file
 
The '.startswith(" ")' operator checks whether a specific substring is present in a string.
It returns True if the substring is found in the string, and False otherwise.
'''

file = "applephotos"
print(file.startswith("pl"))     #return false
print(file.startswith("apple"))     #return true


#another use of .startswith(" ") function
filename = input("Take the file name as input: ")

if filename.startswith("fruit"):
    print("It is a list of fruits")

elif filename.startswith("flower"):
    print("It is a list of flowers")

elif filename.startswith("food"):
    print("It is a list of foods")

elif filename.startswith("devices"):
    print("It is a list of devices")

else:
    print("It is a random list")


