"""
This script defines a function, boxString, which prints a boxed representation of a string. 
If the string is empty, the function terminates early using a return statement. 
The function demonstrates the use of return both for terminating execution and without returning 
a value.
"""
def boxString(contents) :
    n = len(contents)
    
    if n == 0:
        return      #this return will terminate the function with immediately if n==0
    
    print("-" * (n+2))
    print("!" + contents + "!")
    print("-" * (n+2))
    return          #using Return function without any value

boxString("Hello")