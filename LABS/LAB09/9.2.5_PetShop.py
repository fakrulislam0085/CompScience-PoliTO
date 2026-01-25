def discount(prices, is_pet) : 
    total = 0   # total prices of products that are not animals

    if is_pet.count("N") >= 5 and is_pet.count("Y") >= 1 : 
        for i in range(len(prices)) : 
            if is_pet[i] == "N" : 
                total += prices[i] 
        
        # calculate the discount
        discount = total * 0.2      #20% discounts on other products total prices
        print(f"\nYou got a discount of ${discount}😎\n")

    else :
        print("Sorry you need to buy at least 5 other products besides at least one animals to have a discount!🤷‍♀️\n")

def main() : 
    prices = [] 
    is_pet = []
    sentinelValue = -1 

    while True :
        try :
            price = float(input("Enter the product price: ")) 
            break
        except ValueError : 
            print("Please Enter a real Number🥴") 
            continue


    while price != sentinelValue : 
        prices.append(price) 

        pet = input("Is it animal?(Y/N): ").strip().upper()
        is_pet.append(pet)
        
        # take the next price with proper error handling
        while True :
            try :
                price = float(input("Enter the product price: ")) 
                break
            except ValueError : 
                print("Please Enter a real Number🥴") 
                continue
        
    discount(prices, is_pet) 

if __name__ == "__main__": 
    main() 



