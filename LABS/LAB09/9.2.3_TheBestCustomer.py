def name_of_best_customer(sales, customers) :
    if len(sales) > 0 :     # Checking edge case here
        highestAmount = max(sales)
        bestMan = ""

    for i, amount in enumerate(sales) : 
        if amount == highestAmount : 
            bestMan = customers[i] 
    
    return bestMan 

def main() : 
    sales = []      # the amount of the shopping made by the customer
    names = []      # the name of the customer

    try :
        amount = float(input("Enter the amount spent by Customer: ")) 
    except ValueError : 
        print("Please Enter a valid number.\n") 

    sentinel_val = 0        # From the question
    while amount != sentinel_val : 
        sales.append(amount) 
        try: 
            name = input("Enter the name of the customer: ") 
            if name.strip() == "" :
                raise ValueError 
            names.append(name)  

        except ValueError :
            print("Enter a name, Please!\n") 
            continue 
        
        amount = float(input("Enter the amount spent by Customer: ")) 

    # after each acquisition print the best customer name 
    bestMan = name_of_best_customer(sales, names) 
    print(f"\n\nThe best customer for the day is {bestMan.upper()}\n")   
    
if __name__ == "__main__" : 
    main()