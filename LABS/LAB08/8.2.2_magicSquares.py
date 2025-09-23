def magic_squares(matrix) : 
    #1. checking that there are all and only the numbers 1,2,...,16 
    all_elements = [element for row in matrix for element in row]  # Flatten

    if sorted(all_elements) != list(range(1, 17)):
        return False

    #2. The sums of the rows, columns, and diagonals are all equal to each other
    magicSum = sum(matrix[0])

    # Checking row's sum
    for row in matrix :     
        if sum(row) != magicSum : 
            return False 

    # Checking col's sum 
    for col in range(4) : 
        colSum = sum(matrix[row][col] for row in range(4))
        if colSum != magicSum :
            return False 

    # Checking the diagonal's sum 
    primaryDiagonalSum = sum(matrix[i][i] for i in range(4)) 
    secondaryDiagonalSum = sum(matrix[i][3-i] for i in range(4)) 

    if primaryDiagonalSum != magicSum or secondaryDiagonalSum != magicSum : 
        return False 

    return True 

def main() : 
    valueList = list(map(int, input("Enter the values(up to 16): ").split()))

    matrix = [] 
    row = [] 
    cnt = 0 

    for element in valueList : 
        cnt += 1 
        row.append(element) 

        if cnt == 4 : 
            matrix.append(row) 
            cnt = 0 
            row = [] 

    for row in matrix : 
        for element in row : 
            print(element, end=" ")
        print()
    print() 

    result = magic_squares(matrix) 

    if(result) : 
        print("It is a 4x4 Magic Squares.")
    else :
        print("It is not a 4x4 Magic Squares.")

if __name__ == "__main__" : 
    main() 
