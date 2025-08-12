import sys

def main() : 
    user_input = input("Enter the integer: ")
    sentinel_str = "" 

    partial_sum = 0
    max_val, min_val = 0, sys.maxsize   # import sys 
    odd_val, even_val = 0, 0 

    while user_input != sentinel_str : 
        partial_sum += int(user_input)
        
        if int(user_input) < min_val : 
            min_val = int(user_input)
        if int(user_input) > max_val : 
            max_val = int(user_input)
         
        if int(user_input) % 2 == 0 : 
            even_val += 1 
        else :
            odd_val += 1 
        
        print(f"I.  Partial Sum: {partial_sum:>11}") 
        print(f"II.  {'Maximum value':18}: {max_val:>3}   |  {'Minimum value':18}: {min_val:>3}")
        print(f"III. {'Total Even Values':18}: {even_val:>3}   |  {'Total Odd Values':18}: {odd_val:>3}")
        
        user_input = input("\nEnter the integer: ")
    
    print("Terminate the program by entering ENTER💀")

if __name__ == "__main__" : 
    main() 