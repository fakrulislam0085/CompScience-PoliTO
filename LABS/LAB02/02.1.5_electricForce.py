# How to write scientific numbers in python-> read the readme.md file
import math 

EPSILON = 8.854e-12   # Farad/meter (8.854 * 10^-12)
PI = math.pi 

def relativeForce(q1, q2, r) : 
    """Compute Coulomb's force (N) between charges q1 and q2 at distance r (m)."""
    # Coulomb's law: F = (q1 * q2) / (4 * π * ε0 * r^2)
    force = (q1 * q2) / (4 * PI * EPSILON * r**2)

    print(f"The relative force between Q1 and Q2 is {force:.2e} Newtons")

def main() : 
    """Read inputs (C, m) from user and print the resulting force."""
    q1, q2 = map(float, input("Enter the charges(in Coulombs, separated by space): ").split())
    r = float(input("Enter the distance between the charges(in meter): "))
    
    relativeForce(q1, q2, r)

if __name__ == "__main__" : 
    main()


