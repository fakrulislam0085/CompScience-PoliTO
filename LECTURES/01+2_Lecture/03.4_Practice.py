#not all floating-point numbers have an exact representation 
price = 4.35
quantity = 100
total = price * quantity    #Should be 100 * 4.35 = 435.00
print(total)                # prints 434.99999999999994



#arithmatic expression in python
from math import *

x = 10
y = 20

result1 = (x+y) / 2
result2 = (x+y) // 2
result3 = x*y / 2
result4 = (1 + x/100) ** 2
result5 = sqrt(y**2 - x**2)
result6 = (x + y) * pi      #pi is a constant declared in math module

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)