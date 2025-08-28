"""
This program demonstrates the use of `for` loops in Python with different containers and ranges. 
It iterates over a string to print each character and uses the `range()` function to showcase 
various loop configurations, including initialization, condition, and increment/decrement.
"""

cityName = "Roma"

for letter in cityName :
    print(letter, end=" ")

#range container
num = 5

print()
for i in range(num) :       #num excluded, 0 to num-1
    print(i, end=" ")

print()
for i in range(1, num) :    #num excluded, initialization, condition   
    print(i, end=" ")

print()
for i in range(2, num, 2) :    #initialization, condition, increment/decrement
    print(i, end=" ")

print()
for i in range(num, 0, -1) :
    print(i, end=" ")