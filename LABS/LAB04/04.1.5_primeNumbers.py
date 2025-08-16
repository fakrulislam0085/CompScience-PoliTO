from math import sqrt

def is_prime(n) : 
    # if we look at the math, we need values between 2 and the 
    # square root of the number we're looking for and then If we divide our n by these 
    # numbers and if we find out that the n is divisible then it's not prime. Simple! Easy-peasy! 

    if n == 2 : 
        return True 
    else : 
        start_val = 2 
        end_val = int(sqrt(n))

        for i in range(start_val, end_val+1, 1) : 
            if n%i == 0: 
                return False
        return True

def main() : 
    n = int(input("Enter an integer to check if it is prime or not: "))

    ans = is_prime(n)  
    print(f"{n} is Prime: {ans}")

if __name__ == "__main__" : 
    main() 