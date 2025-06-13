"""
Program: Salary Calculator with Sentinel Value
Description:
    This program calculates the total earnings based on user input. 
    The user inputs salaries, and the input process stops when a negative value (-1) is entered. 
    The program then displays the total earnings.
"""


#Code 
done = False 
totalEarnings = 0.0
while not done :
    value = float(input("Enter a salary or -1 to finsish: "))
    if value < 0.0 :
        done = True
    else :
        totalEarnings += value
print("Total Salary:",totalEarnings)