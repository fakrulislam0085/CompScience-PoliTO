"""
This program calculates the average of a series of numerical values entered by the user.

Key functionalities:
1. The user is prompted to enter values one by one.
2. The loop continues until the user presses Enter without providing any input (an empty string acts as the sentinel value to terminate the loop).
3. Each valid numerical input is converted to a float, added to the total, and the count of values is incremented.
4. After the loop ends:
   - If at least one value was entered, the program calculates the average by dividing the total by the count.
   - If no values were entered, the average is set to 0.0.
5. The program then displays the calculated average.

This program demonstrates the use of a sentinel value (empty string) to control a loop and basic arithmetic operations for calculating averages.
"""
#code
total = 0.0
count = 0
inputStr = input("Enter the value:")

#use sentinel string to exit the loop
while inputStr != "":
    value = float(inputStr)
    total += value
    count += 1
    inputStr = input("Enter the value: ")

if count > 0 :
    average = total / count
else :
    average = 0.0
print("Average is:",average)