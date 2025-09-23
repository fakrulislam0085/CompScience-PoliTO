def calculate_financial_aid(inc, ch) : 
    if 30000 <= inc < 40000 and ch>=3 : 
        return 1000 * ch 
    elif 20000 <= inc < 30000 and ch >= 2 : 
        return 1500 * ch 
    elif inc < 20000 : 
        return 2000 * ch 
    return 0
    
def main() : 
    sentinel_val = -1 

    while True :   
        income_per_annum = float(input("Enter the annual income of your family: ")) 
        number_of_children = int(input("How many children do you have?: ")) 

        if income_per_annum == sentinel_val or number_of_children == sentinel_val : 
            print("Successfully exited from the calculation!")
            break 

        total_allocation = calculate_financial_aid(income_per_annum, number_of_children)
        print(F"\nYou got a total allocation of ${total_allocation}\n")

if __name__ == "__main__" : 
    main() 
