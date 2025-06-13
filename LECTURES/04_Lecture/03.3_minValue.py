"""
This program finds the lowest value entered by the user. 
The loop continues until the user presses Enter (empty input), 
and the minimum value is displayed at the end.
"""
lowest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")

while inputStr != "" :
    value = int(inputStr)
    if value < lowest :
        lowest = value
    inputStr = input("Enter a value: ")
    
print(lowest)