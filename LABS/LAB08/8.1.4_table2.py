def main() : 
    m, n = map(int, input("Enter the rows and columns: ").split())
    table = []

    #i. initialize the table with zeros 
    table = [[0 for j in range(n)] for i in range(m)]
    print(table)

    #ii. Fill the entire table with ones 
    table = [[1 for _ in range(n)] for _ in range(m)] 
    print(table) 

    #iii. fill the table by alternating 0 and 1 in a checkerboard pattern 
    table = [[0 if (i+j)%2==0 else 1 for j in range(n)] for i in range(m)]
    print(table)

    #iv. fill with 0 only the top and bottom rows, leaving the rest of the table unchanged
    table = [[0 if (i==0 or i==m-1) else table[i][j] for j in range(n)] for i in range(m)]
    print(table)

    #v. fill with 1 only leftmost and rightmost columns, leaving the rest of the table unchanged 
    table = [[1 if (j==0 or j==n-1) else table[i][j] for j in range(n)] for i in range(m)] 
    print(table) 

    #vi. calculate and print the sum of all the elements 
    s = sum(sum(row) for row in table)
    print(f"Sum of the table: {s}") 


if __name__ == "__main__" : 
    main() 


