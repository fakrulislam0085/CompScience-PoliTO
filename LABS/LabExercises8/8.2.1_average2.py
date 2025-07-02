def neighbor_average(values, row, column) : 
    count = 0 
    total = 0

    for i in range(row - 1, row + 2):  # alternative: for i in [row-1, row, row+1]:
        for j in range(column - 1, column + 2):
            # we must count the element if:
            # - it is not the "center" element itself
            # - it is not outside the table
            if (i, j) != (row, column) and 0 <= i < len(values) and 0 <= j < len(values[i]):
                total = total + values[i][j]
                count = count + 1

    return total / count

def main() : 
    # We can also use list comprehension 
    w, h = 4, 4 
    valuesTable = [[x+1 for i in range(w)] for x in range(h)]

    #print the table in line-by-line creating a box- using list_comprehension
    for row in valuesTable :
        print('|'.join([f'{item:^5d}' for item in row]))  # create a temp list of string-formatted numbers

    # Demonstrate that neighbor average works correctly 
    print(f"The average at (0,0) is {neighbor_average(valuesTable, 0, 0):.2f}")
    print("The average at (1,2) is", neighbor_average(valuesTable, 1, 2))
    print("The average at (3,2) is", neighbor_average(valuesTable, 3, 2))


if __name__ == "__main__" : 
    main() 