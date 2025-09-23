from math import sqrt

def is_prime(n) : 
    # Only test divisors from 2 up to floor(sqrt(n)).
    # If any divisor in that range divides n evenly, n is not prime.
    # This function assumes n >= 2; n == 2 is handled above.

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