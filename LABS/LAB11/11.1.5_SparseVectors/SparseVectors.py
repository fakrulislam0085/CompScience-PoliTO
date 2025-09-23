"""SparseVectors: utility for summing sparse vectors represented as dicts.

Each sparse vector is a dictionary mapping index -> value. The function
`sparse_array_sum(a, b)` returns a new dictionary representing the element-wise
sum of the two sparse vectors.
"""

def sparse_array_sum(a, b) : 
    resultDict = dict(a) 

    for key in b : 
        if key in resultDict :
            resultDict[key] += b[key]
        else :
            resultDict[key] = b[key]
        
    return resultDict

def main() : 
    # Two sparse dictionary
    a = {5: 4, 9: 2, 10: 9}
    b = {5: 4, 8: 4, 10: 4}

    sum_of_a_b = sparse_array_sum(a, b) 

    print(f"A is: {a}")
    print(f"B is: {b}")
    print(f"The sum of a + b as a dictionary: {sum_of_a_b}")

if __name__ == "__main__" : 
    main() 