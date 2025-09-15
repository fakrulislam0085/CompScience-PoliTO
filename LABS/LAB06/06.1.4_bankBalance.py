def calculate_future_balance(x, r, n) :
    x_future = x * (1+r/100)**n     # y = xr^n 
    print(f"In {n} years, ${x} will be ${x_future:.2f}")

def main() : 
    x = float(input("Enter the initial balance: ")) 
    r = float(input("Enter the annual interest rate: ")) 
    n = float(input("Enter the number of years: ")) 

    calculate_future_balance(x, r, n) 

if __name__ == "__main__" : 
    main() 