"""
This program formats a credit card number by removing spaces and dashes. 
It iterates through the input string, skips spaces and dashes, and builds a new string with the remaining characters.
"""
userInput = input("Enter the Credit Card Number: ")     # 1234-5678- 9012-3456

creditCardNumber = ""

for char in userInput :
    if char == " " or char == "-" :
        continue
    else:
        creditCardNumber += char
    
print(f"Formatted Credit Card Number: {creditCardNumber}")