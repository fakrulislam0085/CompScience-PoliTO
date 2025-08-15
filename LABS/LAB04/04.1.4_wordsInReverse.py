def main() : 
    word = input("Enter the Word: ") 

    reverse_word = word[::-1]
    capital_letters = [letter for letter in word if letter.isupper()]
    uppercase_reverse = ''.join(capital_letters[::-1])

    print(f"I.  The word backwards:                         {reverse_word}")
    print(f"II. Uppercase letters starting from the end:    {uppercase_reverse}")

if __name__ == "__main__" : 
    main() 