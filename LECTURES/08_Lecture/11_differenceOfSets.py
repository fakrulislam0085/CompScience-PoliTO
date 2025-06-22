#The difference of two sets results in a new set that contains only the elements that are unique to the first set.
#The difference() method returns a new set containing only the elements that are unique to the first set.

# Example 1
number1 = {1, 2, 3, 4}
number2 = {2, 8, 9, 1}
number  = number1.difference(number2)
print(number)


# Example 2
italianFlag = {"Green", "White", "Red"}
britishFlag = {"Blue", "White", "Red"}
flag1 = britishFlag.difference(italianFlag)
flag2 = italianFlag.difference(britishFlag)
print(flag1)
print(flag2)