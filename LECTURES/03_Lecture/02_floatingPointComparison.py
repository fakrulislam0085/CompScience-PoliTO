#common error
'''
Floating-point numbers have only a limited precision, and
calculations can introduce roundoff errors.
▪ You must take these inevitable roundoffs into account when
comparing floating point numbers.
'''

from math import *
x = sqrt(2.00)
if x*x == 2.0:
    print("sqrt(2.00) squared is 2.0")
else:
    print("sqrt(2.00) squared is not 2.0 but", x*x)




#Using Epsilon for Floating-Point Comparison
'''
in Python programming, epsilon often represents a very small number close to zero, 
typically used to handle floating-point precision issues. Due to the limitations
of floating-point arithmetic, direct comparisons between floating-point numbers 
can be unreliable. An epsilon value allows us to check for "close enough" equality 
rather than exact equality.
'''
epsilon = 1e-14     #declare EPSILON
x = sqrt(2.00)
if abs(x*x - 2.00) < epsilon:
    print("sqrt(2.00) squared is 2.0")
else:
    print("sqrt(2.00) squared is not 2.0 but", x*x)



#ANOTHER EXAMPLE
a = 0.1 + 0.2
b = 0.3
if abs(a - b) < epsilon:
    print("a and b are close enough to be considered equal.")
else:
    print("a and b are not equal.")
