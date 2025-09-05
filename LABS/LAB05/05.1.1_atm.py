CORRECT_PIN = 1234

def main() : 
    attempts = 0 

    while True :
        try : 
            user_input = int(input("Enter your PIN: ")) 
            attempts += 1 

            if user_input == CORRECT_PIN : 
                print("Your PIN is correct.\n")
                break
            else: 
                if attempts < 3 :
                    print(f"After {3 - attempts} more attempts your card will be blocked.\nPlease enter the correct PIN.\n")
                else : 
                    print("Your bank card is blocked. Contact to your bank please!")

        except ValueError :
            print("Your PIN is numeric. Please, try again!\n")

if __name__ == "__main__" : 
    main() 
