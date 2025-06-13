"""
This program prints a table of powers (x¹, x², x³, x⁴) for numbers from 1 to 10. 
It includes headers and formats the output in aligned columns for better readability.
"""
#print headers
print("    x¹   x²   x³   x⁴")
print(" "*4 + '*' * 20)     #4 spaces + 20 stars

#printing row coloum
for i in range(1, 11) :
    print(f"{i**1:5} {i**2:5} {i**3:5} {i**4:5}")


'''
f"{value:5}":

The :5 inside the f-string specifies that the value should occupy 5 spaces.
If the value has fewer digits, it is right-aligned within those 5 spaces, and extra spaces are added to the left.
This ensures that all values in the column are aligned vertically.
'''