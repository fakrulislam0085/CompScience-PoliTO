"""
This program finds the position of the first and last digit in a given string. 
It uses loops to check each character:
1. The first loop stops when the first digit is found or the end of the string is reached.
2. The second loop starts from the end of the string and stops when the last digit is found or the beginning is reached.
"""
#find the position of the first digit in a string
string = input("Write the string: ")
found = False
position = 0

while not found and position < len(string) :       #if true && true meet, the loop continues
    if string[position].isdigit() :
        found = True
    else:
        position += 1

if found == True :
    print("First digit occurs at position:",position)
else :
    print("The string does not contain a digit.") 



#find the position of the last digit in a string
found = True
pos = len(string) - 1

while found and pos >= 0 :      #if true && true meet, the loop continues
    if string[pos].isdigit() :
        found = False
    else :
        pos -= 1

if found == False :
    print("The last digit occurs at position:", pos)
else:
    print("There is no digit in the string")

