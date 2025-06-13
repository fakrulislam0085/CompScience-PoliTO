import random

def generate_password(l) :
    special_characters = "+-*/?!@#$%&"
    digits = "0123456789"
    lowercaseletters = "abcdefghijklmnopqrstuvwxyz"

    passw = "" 
    while l >= 1 : 
        if l >= 1 :
            char = special_characters[random.randint(0, len(special_characters)-1)]
            passw += char 
            l -= 1 

        if l >= 1 :
            digit = digits[random.randint(0, len(digits)-1)]
            passw += digit
            l -= 1 
            
        if l >= 1 :
            char = lowercaseletters[random.randint(0, len(lowercaseletters) -1)] 
            passw += char 
            l -= 1 
    return passw


def main() :
    length = int(input("Give the length: ")) 

    if length < 4 :
        print("Provide a length of atleast 4 chars.\n")
    else :
        password = generate_password(length) 
        print(f"Password: {password}")

main()