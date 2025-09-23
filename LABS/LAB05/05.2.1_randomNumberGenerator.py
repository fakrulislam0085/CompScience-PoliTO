A = 32_310_901    # Underscores don’t change the value; they just make big numbers easier to read.
B = 1_729
M = 2e24

def main() : 
    r_old = int(input("Enter the initial value(the seed): "))

    for _ in range(100) : 
        r_new = (A * r_old + B) % M 
        r_old = r_new 

        print(f"The new numbers is {r_new:.3f}")

if __name__ == "__main__" : 
    main() 

# Python supports underscores in integer and float literals (e.g. 1_000_000, 3.14_15) since Python 3.6.

