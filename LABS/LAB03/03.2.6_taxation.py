def taxCalculator(income, status) : 
    
    if status == "UNMARRIED" : 
        # ❌If income in (0, 8000) -> This is a common mistake for a range check. To check a value in a range, use 'range()'
        if 0 <= income < 8000 : 
            tax = income * 10/100 
        elif 8000 <= income < 32000 : 
            tax = 800 + (income - 8000) * 15/100 
        else : 
            tax = 4400 + (income - 32000) * 25/100 
            
    else :      # Status = "MARRIED" 
        if 0 <= income < 16000 : 
            tax = income * 10/100 
        elif 16000 <= income < 64000 : 
            tax = 1600 + (income - 16000) * 15/100 
        else : 
            tax = 8800 + (income - 64000) * 25/100 
    
    return tax 

def main() : 
    income = float(input("Enter your income: ")) 
    status = input("Enter your marital status(Married/Unmarried?): ").upper() 

    ans = taxCalculator(income, status) 
    
    print(f"Your payable tax is = {ans}")
    
if __name__ == "__main__" : 
    main() 