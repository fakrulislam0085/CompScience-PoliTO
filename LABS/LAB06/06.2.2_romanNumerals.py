"""Roman numeral converter.

Provides a small utility to convert Roman numerals (string) to decimal integers.
Run the script and enter a Roman numeral when prompted; the decimal value
will be printed. """

def roman_value(ch) : 
    values = { 
        'I' : 1, 
        'V' : 5, 
        'X' : 10, 
        'L' : 50, 
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    return values.get(ch, 0)    # Return 0 if invalid 

def roman_to_decimal(s) : 
    total = 0 
    i = 0 

    while i < len(s): 
        # Case 1: last char or current char >= next char
        if i == len(s)-1 or roman_value(s[i]) >= roman_value(s[i+1]) : 
            total += roman_value(s[i]) 
            i += 1 
        else : 
        # Case 2: curr char < next char 
            difference = roman_value(s[i+1]) - roman_value(s[i]) 
            total += difference 
            i += 2      # skip 2 char as we calculated 2 char already 
    
    return total 

def main() : 
    roman = input("Enter a Roman numeral: ").upper().strip() 
    decimal = roman_to_decimal(roman) 

    print(f'The decimal value of {roman} is {decimal}') 

if __name__ == "__main__" : 
    main() 

