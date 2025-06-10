from math import sqrt       #imports sqrt, sin, cos, tan function 
from math import *          #imports all math functions
x = 36
y = sqrt(x)
print("The square root of 36 is: ", y)

a = 45
print(tan(a))   #tangent of a in radian
print(sin(a))   #sine of a in radian
print(cos(a))   #cosine of a in radian
print(degrees(tan(a)))      #converts radian to degrees
print(radians(sin(45)))     #converts degrees to radian


c = 87.487941
print(trunc(c))     #truncates floating point value to an integer
print(ceil(c))      #return the ceil value of c
print(floor(c))     #return the floor value of c
print(round(c, 1))     #return the rounded value with n decimal points
