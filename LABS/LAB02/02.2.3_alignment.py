# Read about Alignment in Python from Readme file
# TIP: Use uppercase letters for constant variable names to indicate they shouldn't change.

A = 10      # Constant integer one
B = 20      # Constant integer two 

def main() : 
    summation = A + B 
    difference = A - B
    product = A * B 
    average = summation / 2 
    distance = abs(difference) 
    max_val = max(A, B)
    min_val = min(A, B) 

    # method 1 (vertically left aligned)
    print(f"A. {'The Sum':18} = {' ':>2} {summation}") 
    print(f"B. {'The difference':18} = {' ':>2} {difference}") 
    print(f"C. {'The product':18} = {' ':>2} {product}") 
    print(f"D. {'The average value':18} = {' ':>2} {average}") 
    print(f"E. {'The distance':18} = {' ':>2} {distance}") 
    print(f"F. {'The maximum value':18} = {' ':>2} {max_val}") 
    print(f"G. {'The minimum value':18} = {' ':>2} {min_val}")

    print()     # blank line

    # method 2 (vertically right aligned)
    print(f"A. {'The Sum':18} = {summation:10}") 
    print(f"B. {'The difference':18} = {difference:10}") 
    print(f"C. {'The product':18} = {product:10}") 
    print(f"D. {'The average value':18} = {average:10}") 
    print(f"E. {'The distance':18} = {distance:10}") 
    print(f"F. {'The maximum value':18} = {max_val:10}") 
    print(f"G. {'The minimum value':18} = {min_val:10}")


if __name__ == "__main__" : 
    main() 









