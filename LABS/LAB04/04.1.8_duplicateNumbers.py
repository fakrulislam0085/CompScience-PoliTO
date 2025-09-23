def main() : 
    previous = None     # A placeholder value in Python 
    duplicate = False 

    line = input("Enter a number: ") 

    while line != "" : 
        while True :
            try :
                num = int(line) 
                break
            except ValueError : 
                print(f"Couldn't convert {line} to integer number. Please Enter an integer.")
                line = input("Enter a number: ") 

        if previous != num:
            if duplicate : 
                print(f"Value {previous} is duplicated.")
                duplicate = False 

        else : 
            duplicate = True

        previous = num 
        line = input("Enter a number: ") 

    # If the entered sequence ends with duplicate numbers, the while loop won't print the value 
    if duplicate : 
        print(f"Value {previous} is duplicated.")

if __name__ == "__main__" : 
    main() 
