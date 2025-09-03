def voucher_calculator(x) : 
    if x < 10 : 
        voucher = 0.0
    elif 10 <= x < 60 : 
        voucher = x * 8/100 
    elif 60 <= x < 150 : 
        voucher = x * 10/100 
    elif 150 <= x < 210 : 
        voucher = x * 12/100 
    elif x >= 210 : 
        voucher = x * 14/100 
    
    return voucher
    
def main() : 
    spent = float(input("How much did the customer spend?: ")) 
    result = voucher_calculator(spent) 

    print(f"You win a voucher of {result:.2f}$ on {spent:.2f}$ spending!")

if __name__ == "__main__" : 
    main() 