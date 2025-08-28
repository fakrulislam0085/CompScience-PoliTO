"""
This program detects duplicate adjacent values entered by the user. 
The loop continues until the user presses Enter (empty input) or a duplicate is found. 
If two consecutive values are the same, the program displays a message and stops.
"""
value = int(input("Enter a Number: "))
inputStr = input("Enter a number: ")

while inputStr != "" :
    previous = value 
    newVal = int(inputStr)
    if previous == newVal :
        print("Duplicate Adjacent Detected")
        break
    value = newVal  # update the value to the current input
    inputStr = input("Enter a number: ")