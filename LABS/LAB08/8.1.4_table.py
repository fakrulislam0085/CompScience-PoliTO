def print_table(table) : 
    print(f"Table: {table}")

def main() : 
    m, n = map(int, input("Enter the row(m) and column(n) number: ").split())

    #I. Initialize the table with zeros
    table = [[0 for j in range(n)] for i in range(m)]
    print_table(table)

    #IV. Replace all elements with 1 
    for row in range(m) : 
        for col in range(n) : 
            table[row][col] = 1 
    print_table(table)

    #III. fill the table by alternating 0 and 1 in a checkerboard pattern
    for row in range(m) : 
        for col in range(n) : 
            if (row+col) % 2 == 0 :
                table[row][col] = 0 
            else :
                table[row][col] = 1

    print_table(table)

    #IV. fill with 0 only the top and bottom rows, leaving the rest of the table unchanged;
    for col in range(n) : 
        table[0][col] = 0 
        table[-1][col] = 0

    print_table(table) 

    #V. fill with 1 only leftmost and rightmost columns, leaving the rest of the table unchanged;
    for row in range(m) : 
        table[row][0] = 1 
        table[row][-1] = 1

    print_table(table)

    #VI. Calculate and print the sum of all the elements.
    s = 0 
    for row in table :
        for x in row : 
            s += x 
    #list comprehension: [x for row in table for x in row]
    print(f"Sum of all elements is: {s}")

if __name__ == "__main__" : 
    main()