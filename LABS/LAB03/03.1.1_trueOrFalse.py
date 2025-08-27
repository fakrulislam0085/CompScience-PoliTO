import math 

def main() : 
    # Comparison I
    if 1 == 1: 
        ans = True 
        print(f"Comparison I is {ans}")
    else : 
        ans = False
        print(f"Comparison I is {ans}")

    # Comparison II
    if 1 == 1.0: 
        ans = True 
        print(f"Comparison II is {ans}")
    else : 
        ans = False
        print(f"Comparison II is {ans}")

    # Comparison III
    if 2.0 == math.sqrt(4): 
        ans = True 
        print(f"Comparison III is {ans}")
    else : 
        ans = False
        print(f"Comparison III is {ans}")

    # Comparison IV
    if '1' == 1: 
        ans = True 
        print(f"Comparison IV is {ans}")
    else : 
        ans = False
        print(f"Comparison IV is {ans}")

    # Comparison V
    if 'ciao' == 'Ciao' : 
        ans = True 
        print(f"Comparison V is {ans}")
    else : 
        ans = False
        print(f"Comparison V is {ans}")


if __name__ == "__main__" : 
    main() 