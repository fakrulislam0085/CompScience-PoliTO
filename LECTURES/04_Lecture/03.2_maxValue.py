"""
This program finds the largest value entered by the user. 
The loop continues until the user presses Enter (empty input), 
and the largest value is displayed at the end.
"""
largest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")

while inputStr != "" :
    value = int(inputStr)
    if value > largest :
        largest = value
    inputStr = input("Enter a value: ")
    
print(largest)