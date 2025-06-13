"""
This script demonstrates the use of a global variable in Python.

Functions:
1. withdraw(amount):
   - Accesses and modifies the global variable `balance`.
   - Checks if the withdrawal amount is less than or equal to the current balance.
   - Updates the balance if the condition is met and prints the new balance.

2. main():
   - Defines the withdrawal amount and calls the withdraw function.

Key Concept:
- The `global` keyword is used to access and modify the global variable `balance` inside the withdraw function.
"""

balance = 2000

def withdraw(amount) :
    #this function inteds to access the 'gloval' variablel
    global balance      #If you omit the global declaration, then the balance variable
                        #inside the withdraw function is considered a local variable
    if balance >= amount:
        balance = balance - amount
    print(balance)

def main() :
    amount = 10000 
    withdraw(amount)

main()
