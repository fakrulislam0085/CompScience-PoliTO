def main() : 
    n = int(input("Enter the side length(n): ")) 

    # Printing the full square
    for i in range(n) : 
        for j in range(n) : 
            print("*", end="")
        print() 
    
    # Printing the Rhombus
    print()
    asterisks = 1 
    spaces = n-1 
    line = 2*n - 1 
    for i in range(line) : 
        if i<n :    # Up shape 
            print(spaces*' ' + asterisks*'*')

            if i != n-1 :
                spaces -= 1
                asterisks += 2 

        else :  # Down shape 
            asterisks -= 2 
            spaces += 1 

            print(spaces*' ' + asterisks*'*')

if __name__ == "__main__" : 
    main() 
