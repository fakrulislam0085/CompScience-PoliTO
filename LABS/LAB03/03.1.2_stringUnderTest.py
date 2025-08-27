def main() : 
    user_input = input("Enter your string: ") 

    if user_input.isalpha() : 
        print(f"I. It contains only letters.") 
    
    if user_input.isalpha() and user_input.isupper() :  # See footnote
        print(f"II. It contains only capital letters.") 
    
    if user_input.isalpha() and user_input.islower() :  # See footnote
        print(f"III. It contains only lowercase letters.")

    elif user_input.isdigit() : 
        print(f"IV. It contains only decimal numeric digits.") 

    
    if user_input.isalnum() :
        print(f"V. It contains only letters and digits(alphanumeric).")
    
    if user_input[0].isupper() : 
        print(f"VI. It starts with a capital letter.")
    
    if user_input.endswith('.') : 
        print(f"VII. It ends with a point.")


if __name__ == "__main__" : 
    main() 


# Remember, the difference is:
#   - All alphabetical characters are uppercase => .isupper()
#   - All characters are alphabetical and uppercase => .isalpha() and .isupper()