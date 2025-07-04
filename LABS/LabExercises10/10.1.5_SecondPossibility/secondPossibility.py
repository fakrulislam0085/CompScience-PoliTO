def main() : 
    sentinel = '' 
    floatSum = 0.0 
    wrongInput = 0
    userInput = input("Enter the value(float):")

    while userInput != sentinel : 
        try : 
            userInput = float(userInput) 
            floatSum += userInput 
        
        except : 
            # If the wrongInput is == 2, exit the program 
            wrongInput += 1 
           
            if wrongInput == 2 : 
                break
            else : 
                print("You have inputted a wrong value. Try again!")


        # prompt the user for the next input
        userInput = input("Enter the value(float):")

    print(f"The sum of all the correctly inputted floating values: {floatSum}")

if __name__ == "__main__" : 
    main() 