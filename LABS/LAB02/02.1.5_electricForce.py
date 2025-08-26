# How to write scientific numbers in python-> read the readme.md file

import math 

EPSILON = 8.854e-12   # Farad/meter (8.854 * 10^-12)
PI = math.pi 

def relativeForce(q1, q2, r) : 
    force = (q1 * q2) / (4 * PI * EPSILON * r**2)

    print(f"The relative force between Q1 and Q2 is {force:.2e} Newtons")

def main() : 
    q1, q2 = map(float, input("Enter the charges(in Coulombs, separated by space): ").split())
    r = float(input("Enter the distance between the charges(in meter): "))
    
    relativeForce(q1, q2, r)

if __name__ == "__main__" : 
    main()


