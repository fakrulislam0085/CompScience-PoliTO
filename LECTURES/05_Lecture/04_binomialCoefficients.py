"""
This script calculates binomial coefficients using factorials. 

Functions:
1. binomialCoefficients(x, y, z):
   - Computes the binomial coefficient using the formula C = x // (y * z).
   - Prints the result.

2. factorials(n, m):
   - Calculates the factorials of n, m, and (n - m).
   - Passes these values to the binomialCoefficients function.

3. main():
   - Takes input values for n and m, ensuring n is greater than or equal to m.
   - Calls the factorials function to compute the binomial coefficient.

Execution:
- The main function is called to start the process.
"""
def binomialCoefficients(x, y, z) :
    C = x // (y*z)
    print(C) 

def factorials(n, m) :
    factN = 1
    factM = 1 
    for i in range(1, n+1) :
        factN *= i
    for i in range(1, m+1) :
        factM *= i

    a = n-m 
    factA = 1
    for i in range(1, a+1) :
        factA *= i 

    binomialCoefficients(factN, factM, factA)

def main() :
    n, m = map(int, input().split())        # n is bigger than m
    if m > n:
        print("m cannot be greater than n for binomial coefficients.")
    else :
        factorials(n, m)

main()