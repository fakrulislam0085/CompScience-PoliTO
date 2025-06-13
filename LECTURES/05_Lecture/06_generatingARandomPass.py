"""
This script generates a random password of specified length, ensuring 
it contains at least one special character and one digit. 
It uses random insertion and predefined character sets to create secure passwords.
"""
import random

def insertAtRandom(password, char) :
    #Insert a char at a random position in the password
    position = random.randint(0, len(password))
    return password[:position] + char + password[position : ]


def makePassword(l) :
    #Generates a passWord with specified length with at least one special character and one digit
    #provided list of special characters(from question), then digits and lowercaseletters
    special_characters = "+-*/?!@#$%&"
    digits = "0123456789"
    lowercaseletters = "abcdefghijklmnopqrstuvwxyz"
    
    #start with an empty password:
    password = ""
    
    #add random lowercase letters untill it's length - 2
    for i in range(l - 2) :
        random_index = random.randint(0, len(lowercaseletters)-1)
        password += lowercaseletters[random_index]
    
    #choose one random digits
    random_digit = digits[random.randint(0, len(digits)-1)]

    #choose one random special char
    random_special_char = special_characters[random.randint(0, len(special_characters)-1)]

    #insert the random_digit and random_special_char at randomPosition of our password
    password = insertAtRandom(password, random_digit)
    password = insertAtRandom(password, random_special_char)

    return password  #return our password


def main():
    length = int(input("Read the length: "))

    if length < 4 :
        print("Password length must be at least 4 characters")
    else :
       password = makePassword(length)
       print("Generate Password:", password)

#run the main function 
main()