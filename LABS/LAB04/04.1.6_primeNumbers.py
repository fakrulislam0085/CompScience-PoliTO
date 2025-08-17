import math 

def is_prime(x) : 
    init_val = 2 
    last_val = int(math.sqrt(x))

    for i in range(init_val, last_val+1, 1) : 
        if x%i == 0 : 
            return False 
    return True 

def show_prime(n) : 
    print(f"All prime numbers between 1~{n}:")

    for i in range(2, n+1) : 
        ans = is_prime(i)
        if ans : 
            print(i) 

def main() : 
    n = int(input("Enter an int: "))
    show_prime(n) 

if __name__ == "__main__" : 
    main() 
