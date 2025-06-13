"""
This program demonstrates the use of the `while` loop in Python through two examples.

Key functionalities:
1. First Example:
   - Uses a `while` loop to increment a counter and accumulate a total until the total reaches 10.
   - Prints the current counter value and the total at each iteration.

2. Second Example:
   - Uses a `while` loop to repeatedly prompt the user for input until a specific condition is met.
   - Stops the loop if the user enters 0.
   - Displays the entered number along with its position in the sequence.

These examples illustrate basic control flow and conditional logic using `while` loops.
"""
# first example
i = 0
total = 0

while total < 10:
    i = i+1
    total = total + i
    print(i, total)


#second example
count = 0
ok = True

while count<10 and ok :
    a = int(input("insert the number: "))
    if a == 0:
        ok = False
    print(f'Number {count +1} = {a}')
    count = count + 1