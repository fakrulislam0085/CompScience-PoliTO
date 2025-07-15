from math import sqrt, floor 

def main() : 

    n = int(input("Enter a positive integer: ")) 

    primes = set(range(2, n+1)) 

    for i in range(2, floor(sqrt(n)) + 1) : 
        for j in range(i**2, n+1, i) : 
            primes.discard(j) 
    
    print("There are", len(primes), "primes less than or equal to", n, ":")
    for p in sorted(primes) : 
        print(" ", p) 

if __name__ == "__main__" :
    main() 

