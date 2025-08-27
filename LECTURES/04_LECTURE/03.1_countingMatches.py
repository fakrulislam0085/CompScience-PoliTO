"""
This program counts the number of negative values entered by the user.

Key steps:
1. The user enters values one by one.
2. The loop stops when the user presses Enter (empty input).
3. Negative values are counted and displayed at the end.
"""
#code
inputSTr = input("Enter value: ")
negatives = 0


while inputSTr != "" :
    Value = int(inputSTr)
    if Value < 0 :
        negatives += 1
    inputSTr = input("Enter the value: ")

print("There are", negatives, "negative Values!")
