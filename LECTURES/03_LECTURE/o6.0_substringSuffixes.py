'''
This program takes a file name as input and tells us what types of file it is.
In this program, we have used ".endswith(" ")" function to determine the last substring of our file
 
The '.endswith(" ")' operator checks whether a specific substring is present in a string.
It returns True if the substring is found in the string, and False otherwise.
'''

file = "applephotos"
print(file.endswith("ppl"))     #return false
print(file.endswith("tos"))     #return true


#another use of .endswith(" ") function
filename = input("Take the file name as input: ")

if filename.endswith(".docs"):
    print("It is a google docs file")

elif filename.endswith(".jpeg"):
    print("It is a photo file")

elif filename.endswith(".pdf"):
    print("It is a pdf file")

elif filename.endswith(".word"):
    print("It is a microsoft word file")

else:
    print("It is a random file")


