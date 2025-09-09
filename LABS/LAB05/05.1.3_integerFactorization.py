def main() : 
    number = int(input("Enter the number: ")) 

    factor = 2      # First prime 
    print(f"The prime factors of {number} are: ")

    while number > 1 : 
        if number % factor == 0 : 
            print(factor) 
            number = number//factor 
        else : 
            factor += 1 
            
if __name__ == "__main__" : 
    main() 


'''
💥 We're not checking whether factor is prime — we don't need to!
Because: all the composite numbers will be skipped automatically when they don't divide the root number.

👉To be precise, Composite numbers fail the if check, and get skipped anyway.
'''




