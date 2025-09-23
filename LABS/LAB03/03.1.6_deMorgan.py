# Demonstrates De Morgan's laws by comparing each boolean expression with its equivalent
def main() : 
    x = int(input("Enter an int: "))
    print() 

    # I. not (x>0 and x<100)
    expr1 = not (x>0 and x<100)
    demorgan1 = (x<=0 or x>=100) 

    # II. not (x>0 or x<100)
    expr2 = not (x>0 or x<100)
    demorgan2 = (x<=0 and x>=100)

    # III. not (x>0 or 100<x)
    expr3 = not (x>0 or 100<x)
    demorgan3 = (x<=0 and 100>=x)

    # IV. not (x>0 and x<100 or x == -1)
    expr4 = not (x>0 and x<100 or x == -1)
    demorgan4 = (x<=0 or x>=100) and x != -1


    # Display the truth values to verify the equivalence pairs
    print(f"I.  not (x>0 and x<100)         = {expr1}")
    print(f"I.  (x<=0 or x>=100)            = {demorgan1}")
    print()

    print(f"II.  not (x>0 or x<100)         = {expr2}")
    print(f"II.  (x<=0 and x>=100)          = {demorgan2}")
    print()

    print(f"III.  not (x>0 or 100<x)        = {expr3}")
    print(f"III.  (x<=0 and 100>=x)         = {demorgan3}")
    print()

    print(f"IV.  not (x>0 and x<100 or x == -1)        = {expr4}")
    print(f"IV.  (x<=0 or x>=100) and x != -1          = {demorgan4}")
    print()

if __name__ == "__main__" : 
    main() 