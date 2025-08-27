"""
This program calculates the average salary based on user input.
The user is prompted to enter salaries one by one, and the loop continues
until the user enters a value <= 0, which acts as a sentinel value to terminate the loop.

Key functionalities:
- Validates that the entered salary is non-negative before processing.
- Accumulates the total salary and counts the number of valid entries.
- Computes and displays the average salary if at least one valid salary is entered.
- Displays a message if no valid salary data is provided.
"""
salary = 0.0
totalsalary = 0.0
monthcount = 0


while salary >= 0.00 :
    #take salary as input and then check is it a valid salary or not
    salary = float(input("Insert salary or -1 to stop the loop: "))
    if salary >= 0.00:
        totalsalary += salary
        monthcount = monthcount + 1

if monthcount > 0:
        average = totalsalary / monthcount
        print(f"Average salary is {average}")
else:
    print("No data was entered")