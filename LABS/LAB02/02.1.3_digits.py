FIVE_DIGIT_INTEGER = 67483

def main() : 
    # Method-1  (converting the int to string and then work on it!)
    print("Method-1:")
    X = str(FIVE_DIGIT_INTEGER) 
    for digit in X: 
        print(digit)
    

    # Method-2 (Ideal method to do this kind of problem) 
    # The '//' operator performs integer (floor) division, returning the quotient without the remainder.
    ones = FIVE_DIGIT_INTEGER // 1           # 67483
    tens = FIVE_DIGIT_INTEGER // 10          # 6748
    hundreds = FIVE_DIGIT_INTEGER // 100     # 674 
    thousands = FIVE_DIGIT_INTEGER // 1000   # 67 
    tens_of_th = FIVE_DIGIT_INTEGER // 10000 #  6 

    # The `%` operator returns the remainder after division (modulus operation)
    print("Method-2:")
    print(f"{tens_of_th % 10}")     # 6 
    print(f"{thousands % 10}")      # 7
    print(f"{hundreds % 10}")       # 4
    print(f"{tens % 10}")           # 8
    print(f"{ones % 10}")           # 3

if __name__ == "__main__" : 
    main()