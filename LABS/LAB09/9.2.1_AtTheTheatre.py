def isSeatAvailable(r, c, priceTable) : 
    if (priceTable[r][c] == 0) :
        return False 
    return True

def main() :
    priceTable = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
            [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
            [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
            [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
            [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
            [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]
    
    #Read the user's choice 
    choice = input("Pick a (S)eat, pick a P(rice) or E(xit?)\nAns: ").upper() 

    while choice != "E": 
        # seat selection by position
        if choice == "S" :
            try : 
                row, col = map(int, input("\nEnter row(0~9) and column(0~8): ").split()) 
                
                # check if the seat is available 
                if (isSeatAvailable(row, col, priceTable) == False) : 
                    print("Sorry! The seat is not available! Choose another seat please.\n") 
                    continue 
                else : 
                    print(f"The seat is sold to you for ${priceTable[row][col]}")
                    priceTable[row][col] = 0 

            except ValueError :
                print("Enter a valid row and column number.\n") 
                continue 
        # seat selection by price
        elif choice == "P" : 
            try: 
                customerPrice = int(input("\nChoose a Price👇:\n10 20 30\n40 50\nAns: "))
                foundAtThePrice = False

                for i in range(len(priceTable)) : 
                    for j in range(len(priceTable[0])) : 
                        if priceTable[i][j] == customerPrice and foundAtThePrice == False : 
                            print(f"The Ticket is yours!\nYour are assigned to seat at row->{i}, column->{j} Position!\n")
                            priceTable[i][j] = 0 
                            foundAtThePrice = True 
                            break
                if foundAtThePrice == False : 
                    print("Sorry, No seat is available at this price.")
                    continue 

            except ValueError :
                customerPrice("Enter a valid price, please!") 
                continue
        # read the next choice
        choice = input("\nPick a (S)eat, pick a P(rice) or E(xit?)\nAns: ").upper() 

    # Display the seating map.
    for row in range(len(priceTable)):
        for col in range(len(priceTable[row])):
            print(f"{priceTable[row][col]:3d}", end="")
        print()

    
if __name__ == "__main__" : 
    main()